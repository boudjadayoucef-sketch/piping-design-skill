"""End-to-end contract test using only deterministic fixtures."""

from pipeline.run import run_pipeline
from vision.provider import StubVisionProvider


def test_photo_to_iso_contract() -> None:
    observation = StubVisionProvider().observe(
        b"fixture",
        source_id="PHOTO-001",
        mime_type="image/jpeg",
    )
    result = run_pipeline(observation, project_id="PROJECT-001")

    assert set(result) == {"observation", "topology", "piping", "engineering", "qa", "iso"}
    assert result["piping"]["project_id"] == "PROJECT-001"
    assert result["iso"]["project_id"] == "PROJECT-001"
    assert result["qa"]["review_required"] is True
    assert result["topology"]["uncertainties"]
