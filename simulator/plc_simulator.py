import time
import random
import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()

URL = "http://localhost:8000/telemetry"
API_KEY = os.getenv("OT_API_KEY")

if not API_KEY:
    raise RuntimeError("OT_API_KEY is not configured")

while True:
    telemetry = {
        "device_id": "PLC-001",
        "temperature": round(random.uniform(20, 35), 2),
        "pressure": round(random.uniform(4, 6), 2),
        "status": "NORMAL"
    }

    data = json.dumps(telemetry).encode()

    request = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "X-API-Key": API_KEY
        },
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        print(response.read().decode())

    time.sleep(5)
