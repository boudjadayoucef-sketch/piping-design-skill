from mcp.server.fastmcp import FastMCP

from .models import PipeSegment
from .tools import validate_pipeline_data

mcp = FastMCP("Piping Design")


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
) -> dict:
    """Create a deterministic pipe segment from two XYZ points and return its length."""
    segment = PipeSegment(
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


# Render runs this module behind Uvicorn. FastMCP exposes the MCP endpoint at /mcp.
# Using an ASGI app avoids relying on FastMCP.run() keyword arguments that vary by version.
app = mcp.http_app(path="/mcp")
