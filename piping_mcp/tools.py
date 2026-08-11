def validate_pipeline_data(pipeline: dict) -> dict:
    errors = []
    warnings = []
    segments = pipeline.get("segments", [])

    for index, segment in enumerate(segments):
        start = segment.get("start")
        end = segment.get("end")
        if not start or not end or len(start) != 3 or len(end) != 3:
            errors.append(f"Segment {index}: invalid XYZ coordinates")
            continue
        if tuple(start) == tuple(end):
            errors.append(f"Segment {index}: zero-length segment")
        if not segment.get("line_id"):
            errors.append(f"Segment {index}: missing line_id")
        if not segment.get("diameter_mm", 0) > 0:
            errors.append(f"Segment {index}: invalid diameter")

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
