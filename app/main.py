import asyncio
from fastapi import FastAPI, Depends
from app.endpoints.characters_router import characters_router


app = FastAPI(title="Characters Service")

@app.on_event('startup')
def startup():
    loop = asyncio.get_event_loop()
    # сходить к зайцу asyncio.ensure_future(rabbitmq.consume(loop))


app.include_router(characters_router, prefix='/api')
