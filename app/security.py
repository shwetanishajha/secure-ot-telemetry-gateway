import os
from dotenv import load_dotenv

from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

load_dotenv()


API_KEY = os.getenv("OT_API_KEY")

api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    return api_key