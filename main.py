from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from app.routers.users import router as users_router


@asynccontextmanager
async def lifespan(_: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield


app = FastAPI(title='My_Project', lifespan=lifespan)

app.include_router(users_router)


@app.get('/', tags=['Страница приветствия'])
async def hello() -> str:
    return "Hello in my project"
