import asyncio
from fastapi import FastAPI, Depends
from app.endpoints.character_router import characters_router
import app.rabbitmq as rabbitmq

app = FastAPI(title="Characters Service")

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(rabbitmq.consume(loop))


app.include_router(characters_router, prefix='/api')
