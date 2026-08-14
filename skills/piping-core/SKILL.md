---
name: piping-core
description: Canonical piping model, deterministic geometry and QA/QC rules for an AI piping design agent.
---

# Piping Core

Use the canonical Piping JSON model as the boundary between AI reasoning and deterministic Python execution.

## Rules

- AI interprets intent; Python performs geometry and validation.
- Never invent missing engineering values.
- Every object has a stable unique ID.
- Preserve source provenance and recognition confidence.
- Validate connectivity after geometry changes.
- Keep CAD adapters separate from the piping model.

## Core objects

Project, Pipeline, PipeSegment, Elbow, Tee, Reducer, Flange, Valve, Instrument, Equipment, Nozzle and Support.

## Canonical flow

Sketch/DXF/DWG -> source model -> normalized Piping JSON -> QA/QC -> geometry/isometric -> DXF/SVG/PDF.
