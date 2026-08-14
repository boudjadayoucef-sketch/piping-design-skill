---
name: piping-sketch-recognition
description: Recognize piping sketches and convert probabilistic vision detections into a validated canonical piping model.
---

# Piping Sketch Recognition

## Recognition pipeline

`image -> visual/OCR detection -> recognition JSON -> topology -> canonical Piping JSON -> QA/QC`

## Detect when possible

- pipe centerlines and polylines
- elbows, tees and reducers
- valves, flanges and instruments
- equipment and nozzles
- dimensions, DN/NPS, tags, line numbers and elevations
- flow arrows and connection points

## Confidence and provenance

Every probabilistic entity should carry `confidence` from 0 to 1 and a source reference such as image region, OCR token or detector ID. Preserve ambiguous detections instead of inventing values.

## Topology

Connections must be explicit. A crossing is not automatically a connection; use symbols, endpoints, layers or explicit recognition evidence.

## AI behavior

The AI/vision model may interpret the image. Python must normalize, validate coordinates, build connectivity and calculate deterministic geometry. The final model must distinguish detected facts from assumptions.
