from math import dist
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


Point3D = tuple[float, float, float]


class SourceRef(BaseModel):
    model_config = ConfigDict(extra="allow")

    kind: str | None = None
    file: str | None = None
    entity_handle: str | None = None
    detector_id: str | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)


class PipeSegment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(default="", min_length=0)
    start: Point3D
    end: Point3D
    diameter_mm: float = Field(gt=0)
    line_id: str = Field(min_length=1)
    material: str | None = None
    source: SourceRef | None = None

    @property
    def length(self) -> float:
        return dist(self.start, self.end)

    def to_dict(self) -> dict[str, Any]:
        data = self.model_dump()
        data["length"] = self.length
        return data


class PipingComponent(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str = Field(min_length=1)
    type: str = Field(min_length=1)
    tag: str | None = None
    position: Point3D | None = None
    confidence: float | None = Field(default=None, ge=0, le=1)
    source: SourceRef | None = None


class Pipeline(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str = Field(min_length=1)
    tag: str | None = None
    spec: str | None = None
    segments: list[PipeSegment] = Field(default_factory=list)
    components: list[PipingComponent] = Field(default_factory=list)


class PipingProject(BaseModel):
    model_config = ConfigDict(extra="allow")

    version: str = "1.0"
    project: dict[str, Any] = Field(default_factory=dict)
    units: str = "mm"
    pipelines: list[Pipeline] = Field(default_factory=list)
