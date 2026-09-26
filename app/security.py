from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

API_KEY = "demo-secure-key"

api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    return api_key