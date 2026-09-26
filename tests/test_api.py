import sys
sys.path.append(".")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_invalid_temperature():
    response = client.post(
        "/telemetry",
        headers={"X-API-Key": "demo-secure-key"},
        json={
            "device_id": "PLC-001",
            "temperature":      500,
            "pressure": 4.8,
            "status": "NORMAL"
        }
    )

    assert response.status_code == 422