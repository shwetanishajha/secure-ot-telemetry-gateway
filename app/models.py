from pydantic import BaseModel, Field


class Telemetry(BaseModel):
    device_id: str = Field(min_length=3, max_length=50)
    temperature: float
    pressure: float
    status: str