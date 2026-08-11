from math import dist
from pydantic import BaseModel, Field

class PipeSegment(BaseModel):
    start: tuple[float, float, float]
    end: tuple[float, float, float]
    diameter_mm: float = Field(gt=0)
    line_id: str

    @property
    def length(self) -> float:
        return dist(self.start, self.end)

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        data["length"] = self.length
        return data

class Pipeline(BaseModel):
    id: str
    segments: list[PipeSegment] = []
