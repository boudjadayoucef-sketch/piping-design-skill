"""Provider-neutral interface for piping vision inference.

Concrete providers should implement ``VisionProvider.detect`` and return the
normalized structures consumed by ``build_observation``. Provider-specific
SDK objects must not cross this boundary.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from .observation_builder import build_observation
from .validate_observation import validate_observation


class VisionProvider(ABC):
    """Contract implemented by a concrete image-vision provider."""

    name = "unknown"

    @abstractmethod
    def detect(self, source: bytes, *, source_id: str, mime_type: str) -> dict[str, Any]:
        """Return provider-normalized detection fields."""
        raise NotImplementedError

    def observe(
        self,
        source: bytes,
        *,
        source_id: str,
        mime_type: str,
        source_type: str = "photo",
    ) -> dict[str, Any]:
        """Run detection and produce a validated observation payload."""
        result = self.detect(source, source_id=source_id, mime_type=mime_type)
        observation = build_observation(source_type=source_type, source_id=source_id, **result)
        errors = validate_observation(observation)
        if errors:
            raise ValueError("invalid observation: " + "; ".join(errors))
        return observation


class StubVisionProvider(VisionProvider):
    """Deterministic provider for tests and integration development."""

    name = "stub"

    def detect(self, source: bytes, *, source_id: str, mime_type: str) -> dict[str, Any]:
        return {
            "objects": [],
            "text": [],
            "relations": [],
            "geometry_hints": [],
            "evidence": [],
        }
