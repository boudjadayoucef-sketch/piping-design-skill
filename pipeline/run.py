"""Orchestrate the complete photo-to-ISO contract without provider-specific AI."""

from __future__ import annotations

from typing import Any

from agents.engineering.agent import review_engineering
from agents.iso.agent import build_iso
from agents.qa.agent import run_qa
from agents.reconstruction.agent import reconstruct_piping
from agents.topology.agent import build_topology


def run_pipeline(observation: dict[str, Any], *, project_id: str) -> dict[str, Any]:
    """Run observation -> topology -> reconstruction -> engineering -> QA -> ISO.

    Vision inference happens before this function through ``VisionProvider``.
    ISO output is representation-only; deterministic geometry generation belongs
    to the MCP/geometry layer and must consume validated engineering data.
    """
    topology = build_topology(observation)
    piping = reconstruct_piping(observation, topology, project_id=project_id)
    engineering = review_engineering(piping)
    qa = run_qa(piping, engineering)
    iso = build_iso(piping, project_id=project_id)

    return {
        "observation": observation,
        "topology": topology,
        "piping": piping,
        "engineering": engineering,
        "qa": qa,
        "iso": iso,
    }
