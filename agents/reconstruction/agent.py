"""Conservative observation/topology to canonical piping reconstruction."""

from __future__ import annotations

from typing import Any


def reconstruct_piping(observation: dict[str, Any], topology: dict[str, Any], *, project_id: str) -> dict[str, Any]:
    components = []
    for node in topology.get("nodes", []):
        obj = next((o for o in observation.get("objects", []) if o.get("id") == node["id"]), {})
        component = {
            "id": node["id"],
            "type": node.get("type", "unknown"),
            "evidence_refs": obj.get("evidence_refs", []),
        }
        if "nominal_diameter" in obj:
            component["nominal_diameter"] = obj["nominal_diameter"]
        if "position" in obj:
            component["position"] = obj["position"]
        if "orientation" in obj:
            component["orientation"] = obj["orientation"]
        components.append(component)

    connections = [
        {
            "id": edge["id"],
            "from": edge["source"],
            "to": edge["target"],
            "type": edge.get("type", "connected"),
            "confidence": edge.get("confidence", 0),
            "evidence_refs": edge.get("evidence_refs", []),
        }
        for edge in topology.get("edges", [])
    ]

    uncertainties = [
        {
            "id": f"unc_{index:04d}",
            "object_id": "",
            "property": item.get("code", "topology"),
            "reason": item.get("reason", "Uncertain reconstruction"),
            "confidence": 0,
            "requires_review": True,
        }
        for index, item in enumerate(topology.get("uncertainties", []), start=1)
    ]

    return {
        "schema_version": "0.1",
        "project_id": project_id,
        "lines": [],
        "components": components,
        "connections": connections,
        "evidence": observation.get("evidence", []),
        "uncertainties": uncertainties,
    }
