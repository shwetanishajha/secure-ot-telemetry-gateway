from fastapi import FastAPI
from app.models import Telemetry

app = FastAPI(
    title="Secure OT Telemetry Gateway",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/telemetry")
def receive_telemetry(data: Telemetry):
    return {
        "message": "Telemetry received",
        "device_id": data.device_id,
        "temperature": data.temperature,
        "pressure": data.pressure,
        "status": data.status
    }