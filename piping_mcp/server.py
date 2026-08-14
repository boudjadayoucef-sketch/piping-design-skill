from mcp.server.fastmcp import FastMCP

from .models import PipeSegment
from .tools import (
    analyze_sketch_input,
    export_dxf_file,
    import_dxf_file,
    sketch_to_piping_model as normalize_sketch_to_piping_model,
    validate_pipeline_data,
)

mcp = FastMCP(
    "Piping Design",
    stateless_http=True,
    json_response=True,
)


@mcp.tool()
def create_pipe_segment(
    start_x: float,
    start_y: float,
    start_z: float,
    end_x: float,
    end_y: float,
    end_z: float,
    diameter_mm: float,
    line_id: str,
    segment_id: str = "SEG-001",
) -> dict:
    """Create a deterministic pipe segment from two XYZ points and return its length."""
    segment = PipeSegment(
        id=segment_id,
        start=(start_x, start_y, start_z),
        end=(end_x, end_y, end_z),
        diameter_mm=diameter_mm,
        line_id=line_id,
    )
    return segment.to_dict()


@mcp.tool()
def validate_pipeline(pipeline: dict) -> dict:
    """Validate connectivity and basic geometry of a pipeline JSON object."""
    return validate_pipeline_data(pipeline)


@mcp.tool()
def cad_import_dxf(file_path: str) -> dict:
    """Import DXF entities into a raw CAD model while preserving source metadata."""
    return import_dxf_file(file_path)


@mcp.tool()
def cad_export_dxf(pipeline: dict, file_path: str) -> dict:
    """Export canonical pipe segments to a deterministic DXF file."""
    from .tools import export_dxf_file
    return export_dxf_file(pipeline, file_path)


@mcp.tool()
def sketch_analyze(file_path: str) -> dict:
    """Prepare a sketch for an external vision/AI recognizer and return the recognition contract."""
    return analyze_sketch_input(file_path)


@mcp.tool()
def sketch_to_piping_model(recognition: dict, line_id: str = "UNASSIGNED") -> dict:
    """Normalize vision recognition JSON into canonical pipe segments and validate them."""
    return normalize_sketch_to_piping_model(recognition, line_id)


app = mcp.streamable_http_app()
