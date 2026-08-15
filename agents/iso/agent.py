"""Build an ISO-ready representation without inventing geometry."""

from __future__ import annotations

from typing import Any


def build_iso(model: dict[str, Any], *, project_id: str, units: str = "mm") -> dict[str, Any]:
    segments: list[dict[str, Any]] = []
    for line in model.get("lines", []):
        for segment in line.get("segments", []):
            segments.append({"line_id": line.get("id"), **segment})

    components = [
        {
            "id": component.get("id"),
            "type": component.get("type"),
            "position": component.get("position"),
            "orientation": component.get("orientation"),
            "tag": component.get("tag"),
        }
        for component in model.get("components", [])
    ]

    return {
        "schema_version": "0.1",
        "project_id": project_id,
        "units": units,
        "title": "Piping Isometric",
        "segments": segments,
        "components": components,
        "dimensions": [],
        "annotations": [],
        "views": [{"type": "isometric", "source": "canonical_piping_model"}],
        "source_refs": [ref for ref in _evidence_refs(model)],
    }


def _evidence_refs(model: dict[str, Any]) -> list[str]:
    refs: list[str] = []
    for component in model.get("components", []):
        refs.extend(component.get("evidence_refs", []))
    for connection in model.get("connections", []):
        refs.extend(connection.get("evidence_refs", []))
    return list(dict.fromkeys(refs))
