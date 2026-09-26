import logging
import os
from dotenv import load_dotenv

from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("security")


API_KEY = os.getenv("OT_API_KEY")

api_key_header = APIKeyHeader(name="X-API-Key")


def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        logger.warning("Failed API authentication attempt")
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    logger.info("Successful API authentication")
    return api_key