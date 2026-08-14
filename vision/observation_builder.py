"""Provider-neutral helpers for building piping observations.

This module intentionally contains no model inference. Vision providers should
map their detections into these normalized structures before downstream agents
consume them.
"""

from __future__ import annotations

from typing import Any


def build_observation(
    *,
    source_type: str,
    source_id: str,
    objects: list[dict[str, Any]] | None = None,
    text: list[dict[str, Any]] | None = None,
    relations: list[dict[str, Any]] | None = None,
    geometry_hints: list[dict[str, Any]] | None = None,
    evidence: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    """Return a normalized observation payload.

    The function performs only structural normalization; it does not infer,
    validate, or invent engineering values.
    """
    return {
        "observation_version": "0.1",
        "source": {"type": source_type, "id": source_id},
        "objects": objects or [],
        "text": text or [],
        "relations": relations or [],
        "geometry_hints": geometry_hints or [],
        "evidence": evidence or [],
    }
