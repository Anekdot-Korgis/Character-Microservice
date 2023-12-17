import asyncio
from fastapi import FastAPI, Depends, Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import app.rabbitmq as rabbitmq
from app.endpoints.character_router import characters_router
import logging
from multiprocessing import Queue
from logging_loki import LokiQueueHandler

app = FastAPI(title="Characters Service")

class LoggingMiddleware(BaseHTTPMiddleware):
 async def dispatch(self, request: Request, call_next):
    if request.url.path.startswith("/api"):
        print(f"Incoming request: {request.method} {request.url}")
        response: Response = await call_next(request)
        print(f"Outgoing response: {response.status_code}")
    else:
        response: Response = await call_next(request)
    return response

app.add_middleware(LoggingMiddleware)

loki_logs_handler = LokiQueueHandler(
 Queue(-1),
 url="http://loki:3100/loki/api/v1/push",
 tags={"application": "fastapi"},
 version="1",
)

uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.addHandler(loki_logs_handler)

@app.on_event('startup')
def startup():
 loop = asyncio.get_event_loop()
 asyncio.ensure_future(rabbitmq.consume(loop))

app.include_router(characters_router, prefix='/api')
