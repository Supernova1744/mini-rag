from fastapi import FastAPI
from routes import base, data
from helpers.config import get_settings
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient



# app.on_even is deprecated using lifespan instead

@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    yield  # This pauses here during app runtime
    app.mongo_conn.close()  # Cleanup when the app shuts down


app = FastAPI(lifespan=lifespan)

app.include_router(base.base_router)
app.include_router(data.data_router)

