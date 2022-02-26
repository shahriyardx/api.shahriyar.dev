import asyncio

from hypercorn import Config
from hypercorn.asyncio import serve

from app import app

config = Config()
config.bind = "127.0.0.1:8088"

asyncio.run(serve(app, config))
