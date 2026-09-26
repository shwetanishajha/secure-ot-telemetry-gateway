from pydantic import BaseModel, Field


class Telemetry(BaseModel):
    device_id: str = Field(min_length=3, max_length=50)
    temperature: float = Field(ge=-50, le=150)
    pressure: float = Field(ge=0, le=100)
    status: str