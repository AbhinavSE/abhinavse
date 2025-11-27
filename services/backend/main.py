import asyncio
import datetime
import sys
import os
import httpx
from loguru import logger

# Configuration
WEB_SERVICE_URL = os.getenv("WEB_SERVICE_URL", "http://web:3000/internal/update")

logger.remove()
logger.add(
    sys.stdout, 
    colorize=True, 
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>BACKEND</cyan> - <level>{message}</level>"
)

async def backend_process_simulator():
    logger.info(f"Backend started. Target: {WEB_SERVICE_URL}")
    async with httpx.AsyncClient() as client:
        while True:
            await asyncio.sleep(2)
            
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            message = f"<div>[{timestamp}] Update from Backend Container...</div>"
            
            # try:
            #     # logger.trace(f"Sending update: {message}")
            #     resp = await client.post(WEB_SERVICE_URL, json={"message": message})
            #     if resp.status_code != 200:
            #         logger.warning(f"Failed to push update: {resp.status_code} - {resp.text}")
            # except httpx.RequestError as e:
            #     logger.error(f"Connection error to Web service: {e}")
            # except Exception as e:
            #     logger.exception(f"Unexpected error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(backend_process_simulator())
    except KeyboardInterrupt:
        logger.info("Backend stopped.")
