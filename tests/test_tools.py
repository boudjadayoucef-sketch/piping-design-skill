from pathlib import Path

from piping_mcp.models import PipeSegment
from piping_mcp.tools import sketch_to_piping_model, validate_pipeline_data


def test_validate_connected_pipeline():
    result = validate_pipeline_data(
        {
            "segments": [
                {
                    "id": "SEG-001",
                    "start": [0, 0, 0],
                    "end": [1000, 0, 0],
                    "diameter_mm": 150,
                    "line_id": "L-001",
                },
                {
                    "id": "SEG-002",
                    "start": [1000, 0, 0],
                    "end": [1000, 1000, 0],
                    "diameter_mm": 150,
                    "line_id": "L-001",
                },
            ]
        }
    )
    assert result["valid"] is True


def test_pipe_segment_length():
    segment = PipeSegment(
        id="SEG-001",
        start=(0, 0, 0),
        end=(3000, 4000, 0),
        diameter_mm=100,
        line_id="L-001",
    )
    assert segment.length == 5000


def test_sketch_normalization():
    result = sketch_to_piping_model(
        {
            "source": {"file": "demo.png", "pipeline_id": "L-001"},
            "entities": [
                {
                    "id": "DET-001",
                    "type": "pipe",
                    "confidence": 0.97,
                    "geometry": {
                        "start": [0, 0, 0],
                        "end": [1000, 0, 0],
                        "diameter_mm": 150,
                    },
                }
            ],
        }
    )
    assert result["pipeline"]["segments"][0]["line_id"] == "L-001"
    assert result["validation"]["valid"] is True
