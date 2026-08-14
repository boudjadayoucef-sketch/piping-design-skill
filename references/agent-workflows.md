# Agent Workflows

## Sketch to piping

`sketch_analyze -> vision/OCR -> recognition JSON -> sketch_to_piping_model -> validate_pipeline`

The vision model is intentionally external to the deterministic MCP server. This allows the same normalization contract to work with different multimodal models.

## DXF to piping

`cad_import_dxf -> raw CAD model -> CAD interpretation -> canonical Piping JSON -> validate_pipeline`

Never confuse raw DXF JSON with the canonical piping model.

## Piping to DXF

`canonical Piping JSON -> validate_pipeline -> cad_export_dxf`

## Future DWG adapter

`DWG -> CAD conversion service -> DXF/raw CAD -> canonical Piping JSON`

The DWG adapter should remain replaceable and must not become a dependency of the core piping model.
