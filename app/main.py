from fastapi import FastAPI, Security
from app.models import Telemetry
from app.security import verify_api_key

app = FastAPI(
    title="Secure OT Telemetry Gateway",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/telemetry")
def receive_telemetry(data: Telemetry, 
api_key: str = Security(verify_api_key)):
    return {
        "message": "Telemetry received",
        "device_id": data.device_id,
        "temperature": data.temperature,
        "pressure": data.pressure,
        "status": data.status
    }   