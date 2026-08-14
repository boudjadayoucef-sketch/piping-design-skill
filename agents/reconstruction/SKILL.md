---
name: piping-reconstruction
---

# Piping Reconstruction Agent

## Purpose
Transform observations, topology and engineering context into a candidate canonical piping model.

## Input
- observation data
- topology graph
- optional P&ID/CAD/project context
- engineering constraints

## Output
`schemas/piping.json`

## Rules
- Preserve source/evidence references.
- Preserve unresolved properties in `uncertainties`.
- Never fabricate missing dimensions, materials, elevations or coordinates.
- Use deterministic geometry tools for calculated positions, lengths and intersections.
- A reconstruction is not considered validated until it passes the QA contract.
