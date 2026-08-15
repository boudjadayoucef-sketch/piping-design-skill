"""Deterministic engineering gate for the reconstructed model."""

from __future__ import annotations

from typing import Any


def review_engineering(model: dict[str, Any]) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    component_ids = {c.get("id") for c in model.get("components", [])}

    for connection in model.get("connections", []):
        if connection.get("from") not in component_ids or connection.get("to") not in component_ids:
            errors.append({
                "code": "UNKNOWN_CONNECTION_ENDPOINT",
                "message": "Connection references a component that does not exist.",
                "object_id": connection.get("id"),
            })
        if connection.get("confidence", 0) < 0.8:
            warnings.append({
                "code": "LOW_CONNECTION_CONFIDENCE",
                "message": "Connection requires engineering review.",
                "object_id": connection.get("id"),
            })

    for uncertainty in model.get("uncertainties", []):
        if uncertainty.get("requires_review"):
            warnings.append({
                "code": "MODEL_UNCERTAINTY",
                "message": uncertainty.get("reason", "Uncertain model property."),
                "object_id": uncertainty.get("object_id") or None,
            })

    return {
        "errors": errors,
        "warnings": warnings,
        "status": "REJECTED" if errors else ("WARNING" if warnings else "PASS"),
    }
