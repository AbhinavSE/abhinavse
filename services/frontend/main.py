from fastapi import FastAPI, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, StreamingResponse
import uvicorn
import asyncio
import sys
from loguru import logger
from pydantic import BaseModel

# --- Logger Config ---
logger.remove()
logger.add(
    sys.stdout,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
)

app = FastAPI()

# Serve static and templates from local directories
app.mount("/static", StaticFiles(directory="services/frontend/static"), name="static")
templates = Jinja2Templates(directory="services/frontend/templates")

# --- Broadcasting Manager ---
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[asyncio.Queue] = []

    async def connect(self):
        queue = asyncio.Queue()
        self.active_connections.append(queue)
        logger.info(f"Client connected. Active connections: {len(self.active_connections)}")
        return queue

    def disconnect(self, queue):
        if queue in self.active_connections:
            self.active_connections.remove(queue)
            logger.info(f"Client disconnected. Active connections: {len(self.active_connections)}")

    async def broadcast(self, message: str):
        if not self.active_connections:
            return
        
        logger.debug(f"Broadcasting message to {len(self.active_connections)} clients")
        for queue in self.active_connections:
            await queue.put(message)

manager = ConnectionManager()

# --- New Internal Endpoint for Backend ---
class UpdatePayload(BaseModel):
    message: str

@app.post("/internal/update")
async def receive_backend_update(payload: UpdatePayload):
    """Receives updates from the Backend service and broadcasts them."""
    # In a real app, you might verify a secret token here for security
    await manager.broadcast(payload.message)
    return {"status": "received"}

# --- Standard Endpoints ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info(f"Accessing Root Endpoint: {request.client.host}")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    logger.info(f"Accessing About Endpoint: {request.client.host}")
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/stream")
async def stream(request: Request):
    logger.info(f"New stream request initiated from {request.client.host}")
    async def event_generator():
        queue = await manager.connect()
        try:
            while True:
                data = await queue.get()
                yield f"data: {data}\n\n"
        except asyncio.CancelledError:
            logger.warning(f"Stream connection cancelled by {request.client.host}")
            manager.disconnect(queue)

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    logger.info("Starting Uvicorn server...")
    uvicorn.run("services.frontend.main:app", host="0.0.0.0", port=3000, reload=True)
