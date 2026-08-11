from math import dist

from pydantic import BaseModel, ConfigDict, Field


class PipeSegment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    start: tuple[float, float, float]
    end: tuple[float, float, float]
    diameter_mm: float = Field(gt=0)
    line_id: str = Field(min_length=1)

    @property
    def length(self) -> float:
        return dist(self.start, self.end)

    def to_dict(self) -> dict:
        data = self.model_dump()
        data["length"] = self.length
        return data


class Pipeline(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(min_length=1)
    segments: list[PipeSegment] = Field(default_factory=list)
