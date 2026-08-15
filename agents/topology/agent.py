"""Deterministic candidate topology builder.

This module only promotes explicit visual relations into a topology graph. It
never invents geometry or engineering facts. A future topology LLM can provide
additional candidate edges through the same normalized contract.
"""

from __future__ import annotations

from typing import Any


def build_topology(observation: dict[str, Any]) -> dict[str, Any]:
    object_ids = {obj["id"] for obj in observation.get("objects", []) if obj.get("id")}
    nodes = [
        {"id": obj["id"], "type": obj.get("type", "unknown"), "confidence": obj.get("confidence", 0)}
        for obj in observation.get("objects", [])
        if obj.get("id")
    ]
    edges: list[dict[str, Any]] = []
    for index, relation in enumerate(observation.get("relations", []), start=1):
        source = relation.get("source")
        target = relation.get("target")
        if source in object_ids and target in object_ids:
            edges.append({
                "id": f"edge_{index:04d}",
                "source": source,
                "target": target,
                "type": relation.get("type", "connected"),
                "confidence": relation.get("confidence", 0),
                "evidence_refs": relation.get("evidence_refs", []),
                "basis": "observed_relation",
            })

    uncertainties = []
    if not edges and nodes:
        uncertainties.append({
            "code": "NO_OBSERVED_CONNECTIONS",
            "reason": "No explicit visual relations were supplied; connectivity must not be invented.",
            "requires_review": True,
        })

    return {
        "schema_version": "0.1",
        "source_observation": observation.get("source", {}).get("id", ""),
        "nodes": nodes,
        "edges": edges,
        "uncertainties": uncertainties,
    }
