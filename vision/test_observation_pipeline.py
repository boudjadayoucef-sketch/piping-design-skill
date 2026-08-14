"""Executable smoke tests for the provider-neutral observation pipeline."""

from __future__ import annotations

from .provider import StubVisionProvider
from .validate_observation import is_valid_observation


def test_stub_provider_returns_valid_observation() -> None:
    provider = StubVisionProvider()
    observation = provider.observe(
        b"test-image",
        source_id="IMG-TEST-001",
        mime_type="image/jpeg",
    )

    assert observation["source"] == {
        "type": "photo",
        "id": "IMG-TEST-001",
    }
    assert is_valid_observation(observation)
    assert observation["objects"] == []


def test_provider_does_not_leak_sdk_objects() -> None:
    provider = StubVisionProvider()
    result = provider.detect(b"test-image", source_id="IMG-TEST-002", mime_type="image/jpeg")

    assert isinstance(result, dict)
    assert set(result) == {
        "objects",
        "text",
        "relations",
        "geometry_hints",
        "evidence",
    }
