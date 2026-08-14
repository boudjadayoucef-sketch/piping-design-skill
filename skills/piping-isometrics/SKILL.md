---
name: piping-isometrics
description: Generate deterministic isometric drawing data from the canonical piping model.
---

# Piping Isometrics

Use the canonical 3D piping model as input. The AI prepares drawing intent; Python generates geometry and drawing entities.

Include when available: centerlines, fittings, valves, dimensions, elevations, tags, weld numbers, flow direction and BOM/MTO references.

Never fabricate dimensions or component specifications. Return warnings for missing drawing information.
