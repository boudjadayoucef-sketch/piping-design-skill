---
name: piping-topology
---

# Piping Topology Agent

## Purpose
Convert visual observations into a piping connectivity graph without inventing engineering geometry.

## Input
- `schemas/observation.json`
- optional P&ID/project context

## Output
A topology graph or a canonical piping model candidate with:
- stable object IDs
- nodes
- connections
- connection type
- confidence
- evidence references

## Rules
1. Connectivity must be explicit.
2. Unknown connections remain unresolved rather than guessed.
3. Topology is separate from exact XYZ geometry.
4. Do not assign dimensions/materials unless supported by evidence or engineering context.
5. Low-confidence topology must be flagged for QA/review.
