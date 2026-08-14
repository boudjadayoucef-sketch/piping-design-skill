---
name: piping-design
description: Skill for industrial piping engineering with agent-ready vision, reconstruction, topology, geometry, QA/QC and isometric workflows.
---

# Piping Design

Use this skill when designing, coding, reviewing or extending industrial piping software and when converting P&ID, CAD, sketches or photographs into a validated structured piping model.

## Architecture

The skill is organized around a canonical engineering model and explicit agent contracts:

```text
Photo / Sketch / P&ID / DXF
        |
        v
Observation JSON
        |
        v
Topology / Reconstruction
        |
        v
Canonical Piping JSON
        |
        +--> Engineering / Geometry
        +--> QA/QC
        +--> Isometric / MTO / CAD
```

AI agents interpret inputs, select operations and manage uncertainty. Deterministic Python tools perform geometry, connectivity, routing, validation and file generation.

## Agent boundaries

Agents must communicate through versioned schemas and must not silently mutate another layer's representation.

- **Vision**: detects piping objects, visual relations and geometry hints from images.
- **OCR**: extracts text and associates text regions with observations.
- **Topology**: converts observations into a connectivity graph.
- **Reconstruction**: converts observations + topology + engineering context into canonical piping data.
- **Engineering**: applies domain rules and identifies missing or incompatible engineering information.
- **Geometry**: requests deterministic calculations; it does not invent coordinates.
- **QA**: validates the canonical model and returns errors/warnings with evidence.
- **Isometric**: prepares deterministic drawing input from a validated model.
- **Orchestrator**: plans agent/tool calls and routes artifacts; it is not the source of engineering truth.

## Canonical artifacts

### Observation JSON

Observation data describes what was seen or extracted. It is not an engineering model.

It should contain, where available:

- source metadata
- detected objects
- text regions
- visual relations
- geometry hints
- confidence
- evidence references

### Canonical Piping JSON

The canonical piping model is the engineering source of truth. It should contain stable IDs, lines, segments, components, connections and explicit uncertainty/evidence metadata.

Never promote an uncertain observation to engineering truth without recording its source and confidence.

### Evidence

Every inferred or externally observed property should be traceable to an evidence record whenever practical. Do not fabricate evidence.

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

A pipe route consists of connected segments. Each segment should contain, when known:

- start point
- end point
- direction
- length
- diameter
- material
- line ID

Check connectivity after every geometry modification.

## Isometric drawings

The application should derive an isometric representation from the validated 3D piping model.

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

The AI prepares drawing data. The Python graphics engine generates the actual drawing.

## P&ID

P&ID information can be transformed into structured objects:

P&ID → Equipment → Nozzles → Lines → Components → 3D model

Never invent missing engineering information. Mark assumptions and unresolved values explicitly.

## Photo / sketch reconstruction

Do not use a direct `image -> final piping JSON` shortcut.

Use:

```text
image -> observation -> topology/reconstruction -> canonical piping model -> QA
```

Preserve confidence and evidence so a human or future PD&I application can review uncertain properties.

## MTO/BOM

Extract quantities only from the structured model.

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
- unresolved or low-confidence assumptions

## CAD/BIM

Keep CAD/BIM import/export separated from the core piping model.

Preferred architecture:

CAD/BIM file
→ importer
→ observation/raw CAD or normalized piping model
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

## MCP / deterministic tools

MCP tools are the execution boundary for deterministic engineering operations. Agents may request operations such as routing, geometry calculation, connectivity checks and validation, but the tool result is authoritative.

Do not put geometry calculations or engineering validation directly into prompts or UI code.

## Python architecture

Prefer modular Python code with clear interfaces:

```text
models/
schemas/
vision/
topology/
reconstruction/
geometry/
routing/
pid/
cad/
mto/
qa/
isometric/
piping_mcp/
```

Use typed Python models and versioned JSON schemas.

## Important rules

1. AI interprets, plans and selects operations; deterministic code calculates and validates.
2. Never invent missing engineering information. Record uncertainty explicitly.
3. Observation data and canonical engineering data are different artifacts.
4. Every object has a stable unique ID.
5. Prefer schema validation at every agent boundary.
6. Keep CAD/BIM adapters separate from the canonical piping model.
