import os

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


if __name__ == "__main__":
    # Render and similar hosts provide the listening port through PORT.
    port = int(os.getenv("PORT", "8000"))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)
