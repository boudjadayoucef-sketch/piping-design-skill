"""Lightweight structural validation for normalized piping observations."""

from __future__ import annotations

from typing import Any


ALLOWED_SOURCE_TYPES = {"photo", "sketch", "pid", "cad"}


def validate_observation(observation: dict[str, Any]) -> list[str]:
    """Return structural errors without performing engineering inference."""
    errors: list[str] = []

    if observation.get("observation_version") != "0.1":
        errors.append("unsupported observation_version")

    source = observation.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
    else:
        if source.get("type") not in ALLOWED_SOURCE_TYPES:
            errors.append("source.type is invalid")
        if not isinstance(source.get("id"), str) or not source["id"]:
            errors.append("source.id must be a non-empty string")

    for key in ("objects", "text", "relations", "geometry_hints", "evidence"):
        if not isinstance(observation.get(key), list):
            errors.append(f"{key} must be an array")

    for item in observation.get("objects", []):
        if not isinstance(item, dict):
            errors.append("object entry must be an object")
            continue
        if not item.get("id") or not item.get("type"):
            errors.append("object requires id and type")
        confidence = item.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"invalid object confidence: {item.get('id')}")

    for item in observation.get("relations", []):
        if not isinstance(item, dict):
            errors.append("relation entry must be an object")
            continue
        for field in ("source", "target", "type"):
            if not item.get(field):
                errors.append(f"relation requires {field}")
        confidence = item.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append("invalid relation confidence")

    return errors


def is_valid_observation(observation: dict[str, Any]) -> bool:
    return not validate_observation(observation)
