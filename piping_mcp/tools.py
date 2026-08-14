from __future__ import annotations

from pathlib import Path
from typing import Any

from .models import PipeSegment, PipingProject


def validate_pipeline_data(pipeline: dict) -> dict:
    errors: list[str] = []
    warnings: list[str] = []
    segments = pipeline.get("segments", [])
    ids: set[str] = set()

    for index, segment in enumerate(segments):
        sid = segment.get("id") or f"segment-{index + 1}"
        if sid in ids:
            errors.append(f"Segment {sid}: duplicate id")
        ids.add(sid)
        start = segment.get("start")
        end = segment.get("end")
        if not isinstance(start, (list, tuple)) or not isinstance(end, (list, tuple)) or len(start) != 3 or len(end) != 3:
            errors.append(f"Segment {sid}: invalid XYZ coordinates")
            continue
        if tuple(start) == tuple(end):
            errors.append(f"Segment {sid}: zero-length segment")
        if not segment.get("line_id"):
            errors.append(f"Segment {sid}: missing line_id")
        if not segment.get("diameter_mm", 0) > 0:
            errors.append(f"Segment {sid}: invalid diameter")

    for i in range(len(segments) - 1):
        a_end = tuple(segments[i].get("end", []))
        b_start = tuple(segments[i + 1].get("start", []))
        if len(a_end) == 3 and len(b_start) == 3 and a_end != b_start:
            errors.append(f"Segments {i} and {i + 1}: disconnected")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "segment_count": len(segments),
    }


def import_dxf_file(file_path: str) -> dict[str, Any]:
    """Read DXF into a loss-minimizing raw CAD representation."""
    import ezdxf

    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(file_path)

    doc = ezdxf.readfile(path)
    entities: list[dict[str, Any]] = []
    for entity in doc.modelspace():
        item: dict[str, Any] = {
            "handle": entity.dxf.handle,
            "type": entity.dxftype(),
            "layer": entity.dxf.get("layer", "0"),
        }
        if entity.dxftype() == "LINE":
            item["start"] = list(entity.dxf.start)
            item["end"] = list(entity.dxf.end)
        elif entity.dxftype() == "LWPOLYLINE":
            item["points"] = [list(point[:2]) for point in entity.get_points("xy")]
            item["closed"] = bool(entity.closed)
        elif entity.dxftype() in {"CIRCLE", "ARC"}:
            item["center"] = list(entity.dxf.center)
            item["radius"] = entity.dxf.radius
        elif entity.dxftype() == "INSERT":
            item["block"] = entity.dxf.name
            item["insert"] = list(entity.dxf.insert)
        entities.append(item)

    return {
        "format": "dxf",
        "file": str(path),
        "version": doc.dxfversion,
        "entities": entities,
        "entity_count": len(entities),
    }


def export_dxf_file(pipeline: dict[str, Any], file_path: str) -> dict[str, Any]:
    """Generate a simple DXF from canonical pipe segments."""
    import ezdxf

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = ezdxf.new("R2018")
    msp = doc.modelspace()
    segments = pipeline.get("segments", [])
    exported = 0

    if "PIPE" not in doc.layers:
        doc.layers.add("PIPE")

    for segment in segments:
        start = segment.get("start")
        end = segment.get("end")
        if not start or not end:
            continue
        msp.add_line(start, end, dxfattribs={"layer": "PIPE"})
        exported += 1

    doc.saveas(path)
    return {"format": "dxf", "file": str(path), "entity_count": exported, "valid": True}


def analyze_sketch_input(file_path: str) -> dict[str, Any]:
    """Return the contract for a vision/OCR model that will recognize a sketch.

    This function intentionally does not pretend to perform semantic vision. The
    agent or a connected vision model supplies recognition JSON, which is then
    normalized by sketch_to_piping_model.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(file_path)
    return {
        "file": str(path),
        "recognized_by": "external-vision-or-agent",
        "required_output_schema": "schemas/recognition.schema.json",
        "next_tool": "sketch_to_piping_model",
    }


def sketch_to_piping_model(recognition: dict[str, Any], line_id: str = "UNASSIGNED") -> dict[str, Any]:
    """Normalize recognized pipe centerlines into the canonical piping model."""
    segments: list[dict[str, Any]] = []
    warnings: list[str] = []
    for entity in recognition.get("entities", []):
        if entity.get("type") not in {"pipe", "line", "pipe_segment"}:
            continue
        geometry = entity.get("geometry") or {}
        start = geometry.get("start")
        end = geometry.get("end")
        diameter = geometry.get("diameter_mm")
        if not start or not end or not diameter:
            warnings.append(f"Entity {entity.get('id', '?')}: incomplete pipe geometry")
            continue
        segment = PipeSegment(
            id=str(entity.get("id")),
            start=tuple(start),
            end=tuple(end),
            diameter_mm=float(diameter),
            line_id=str(geometry.get("line_id") or line_id),
            source={
                "kind": "sketch",
                "file": recognition.get("source", {}).get("file"),
                "detector_id": entity.get("id"),
                "confidence": entity.get("confidence"),
            },
        )
        segments.append(segment.model_dump())

    pipeline = {"id": recognition.get("source", {}).get("pipeline_id", "SKETCH-001"), "segments": segments}
    validation = validate_pipeline_data(pipeline)
    return {"pipeline": pipeline, "validation": validation, "warnings": warnings}
