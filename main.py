from contextlib import asynccontextmanager
from app.db import models
from app.db.database import engine
from app.routers.users import router as users_router
from app.db.database import Base

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


@asynccontextmanager
async def lifespan(_: FastAPI):

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title='My_Project', lifespan=lifespan)

app.include_router(users_router)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=['Главная страница'])
async def read_index():
    return FileResponse('static/index.html')
