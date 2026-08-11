---
name: piping-design
description: Skill for developing industrial piping software in Python, including piping components, 3D routing, isometric drawings, P&ID data, CAD/BIM interoperability, MTO/BOM and QA/QC.
---

# Piping Design

Use this skill when designing, coding, reviewing or extending a Python application for industrial piping and pipeline design.

## Main capabilities

- Piping component modeling
- 3D pipe routing
- Equipment and nozzle connections
- P&ID data interpretation
- Isometric drawing preparation
- MTO/BOM generation
- Clash detection
- QA/QC
- CAD/BIM interoperability
- JSON project data

## Engineering objects

The application should support at least:

- Project
- Pipeline
- PipeLine
- PipeSegment
- Elbow
- Tee
- Reducer
- Flange
- Valve
- Instrument
- Equipment
- Nozzle
- Support

Every object should have a unique ID.

## Geometry

Use a Cartesian XYZ coordinate system.

Never approximate engineering geometry when the Python geometry engine can calculate it.

The AI should define the operation, while Python performs:

- distances
- vectors
- intersections
- rotations
- transformations
- routing
- collision detection
- lengths

## Routing

A pipe route consists of connected segments.

Each segment should contain:

- start point
- end point
- direction
- length
- diameter
- material
- line ID

Check connectivity after every geometry modification.

## Isometric drawings

The application should be able to derive an isometric representation from the 3D piping model.

Possible information:

- pipe centerlines
- fittings
- valves
- dimensions
- elevations
- tags
- weld numbers
- flow direction
- BOM/MTO

The AI should prepare drawing data. The Python graphics engine should generate the actual drawing.

## P&ID

P&ID information can be transformed into structured objects:

P&ID → Equipment → Nozzles → Lines → Components → 3D model

Never invent missing engineering information. Mark assumptions explicitly.

## MTO/BOM

Extract quantities from the structured model.

Example:

PIPE DN150: 25.4 m
ELBOW DN150: 8
TEE DN150: 2
VALVE DN150: 3
FLANGE DN150: 12

## QA/QC

Check for:

- disconnected segments
- missing IDs
- duplicate tags
- invalid coordinates
- zero-length segments
- incompatible connections
- missing diameters
- missing materials
- potential clashes

## CAD/BIM

Keep CAD/BIM import/export separated from the core piping model.

Preferred architecture:

CAD/BIM file
→ importer
→ normalized piping model
→ geometry engine
→ application

Supported targets may include:

- DXF
- DWG
- IFC
- Revit
- CSV
- Excel
- JSON

## Python architecture

Prefer modular Python code.

Recommended separation:

geometry/
piping/
routing/
isometric/
pid/
cad/
mto/
qa/
models/

Use typed Python models and clear interfaces.

Do not place geometry calculations directly inside UI code.

## Important rule

The Skill provides engineering logic and development guidance.

The Python application is responsible for actual geometry calculations and deterministic results.
