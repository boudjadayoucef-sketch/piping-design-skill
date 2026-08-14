---
name: piping-dxf
description: Import DXF into a raw CAD model, normalize CAD entities into canonical piping JSON, and export piping JSON back to DXF.
---

# DXF Interoperability

## Flow

`DXF -> raw CAD model -> piping interpreter -> canonical Piping JSON`

and

`Piping JSON -> deterministic geometry -> DXF`

## Import rules

- Preserve entity handle, type, layer, block name and source file when available.
- Do not assume that every LINE is a pipe; interpretation must use layers, blocks, connectivity, dimensions and project rules.
- Keep raw CAD data separate from the canonical piping model.
- Report unsupported entities instead of silently dropping them.

## Export rules

- Use the Python DXF adapter.
- Generate valid DXF entities from the canonical model.
- Preserve stable IDs through metadata where possible.
- Return a validation report with entity counts and warnings.

## AI behavior

The AI selects import/normalization/export operations. It must not manually generate DXF syntax.
