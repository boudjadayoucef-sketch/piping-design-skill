# PD&I AI roadmap

## Source baseline

The PD&I workflow dated 21 August 2026 places patches 021–026 around 2D→3D, the component catalogue, professional printing, vision AI, load testing/monitoring, and scalable architecture.

## AI foundation

Introduce the AI foundation between the métier work and the vision workflow:

- versioned `piping-skills`;
- skill registry;
- deterministic engineering validators;
- LangFlow orchestration;
- AI gateway between PD&I and LangFlow;
- asynchronous queue/worker execution;
- structured validation reports;
- human confirmation for vision-derived geometry.

## Target flow

```text
PD&I React
   |
   v
AI Gateway
   |
   v
Async Job Queue
   |
   v
LangFlow
   |
   +--> Vision
   +--> Geometry
   +--> Topology
   +--> Catalog / RAG
   +--> Engineering validators
   |
   v
Structured result
   |
   v
Human validation
   |
   v
PD&I project graph
```

## Alignment with the PD&I roadmap

- Patch 021: provide geometry and clearance skills.
- Patch 022: provide component and compatibility skills.
- Patch 023: expose BOM, quantities, and reporting data.
- Patch 024: use the vision workflow; AI proposes and the user confirms.
- Patch 025: monitor AI jobs and application performance.
- Patch 026: scale the gateway, workers, queues, and data services.

## Non-negotiable boundary

LangFlow orchestrates. It does not become the source of truth for geometry, topology, or engineering rules. Deterministic skills remain authoritative for validation.
