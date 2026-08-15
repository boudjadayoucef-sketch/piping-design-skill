"""QA aggregation for the pipeline."""

from __future__ import annotations

from typing import Any


def run_qa(model: dict[str, Any], engineering_result: dict[str, Any]) -> dict[str, Any]:
    errors = list(engineering_result.get("errors", []))
    warnings = list(engineering_result.get("warnings", []))

    if not model.get("components"):
        warnings.append({"code": "NO_COMPONENTS", "message": "No piping components were reconstructed."})
    if not model.get("connections") and model.get("components"):
        warnings.append({"code": "NO_CONNECTIONS", "message": "No connections were established; ISO generation should require review."})

    status = "REJECTED" if errors else ("WARNING" if warnings else "PASS")
    return {
        "schema_version": "0.1",
        "status": status,
        "errors": errors,
        "warnings": warnings,
        "review_required": bool(errors or warnings),
    }
