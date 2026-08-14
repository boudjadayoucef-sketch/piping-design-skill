---
name: piping-design
description: Core skill for developing industrial piping design and isometric software with AI-assisted sketch recognition, DXF interoperability, deterministic geometry, P&ID, MTO/BOM and QA/QC.
---

# Piping Design Agent Skill

Use this skill when designing, coding, reviewing or extending an industrial piping design and isometric application.

## Architecture

The canonical boundary is:

`Sketch/DXF/DWG -> source model -> canonical Piping JSON -> QA/QC -> geometry/isometric -> DXF/SVG/PDF`

The AI interprets intent and uncertain visual information. Python tools perform deterministic geometry, CAD parsing/export and validation.

## Tool selection

- Sketch/image: `sketch_analyze` then `sketch_to_piping_model`.
- DXF: `cad_import_dxf` then normalize raw CAD entities into Piping JSON.
- DXF generation: `cad_export_dxf`.
- Geometry changes: deterministic Python functions, followed by `validate_pipeline`.
- Never generate CAD syntax manually in an AI response.

## Engineering objects

Support at least Project, Pipeline, PipeSegment, Elbow, Tee, Reducer, Flange, Valve, Instrument, Equipment, Nozzle and Support. Every object has a stable unique ID.

## Geometry and routing

Use Cartesian XYZ coordinates. Python performs distances, vectors, intersections, rotations, transformations, routing, clash detection and lengths. A route is a connected graph of segments and components. Check connectivity after every geometry modification.

## Sketch recognition

Recognition is probabilistic. Preserve confidence and provenance for every detected entity. A crossing is not automatically a connection. Missing dimensions, specifications or tags must remain missing or be marked as assumptions.

## CAD/BIM

Keep CAD/BIM adapters separate from the core model. Preserve source file, entity handle, layer and block metadata when available. DXF is parsed into a raw CAD model before piping interpretation. DWG adapters should convert or delegate to a CAD service rather than contaminate the core model.

## Isometrics

Derive isometric drawing data from the 3D piping model. Include centerlines, fittings, valves, dimensions, elevations, tags, weld numbers, flow direction and BOM/MTO references when available. Python generates actual drawing entities.

## P&ID

Transform structured P&ID information through Equipment -> Nozzles -> Lines -> Components -> 3D model. Never invent engineering information.

## MTO/BOM

Extract quantities from the structured model. Do not estimate quantities from prose when the model can calculate them.

## QA/QC

Check disconnected segments, missing or duplicate IDs/tags, invalid coordinates, zero-length segments, incompatible connections, invalid diameters, missing required attributes and potential clashes.

## Python architecture

Prefer modular packages: `models/`, `geometry/`, `piping/`, `routing/`, `cad/`, `sketch/`, `isometric/`, `pid/`, `mto/`, `qa/`.

The Skill provides engineering logic and development guidance. The Python application is responsible for actual deterministic results.
