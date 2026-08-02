from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import FileResponse
from sqladmin import Admin
from pathlib import Path

from app.db import Base, engine
from app.routers import users_router, dish_router, orders_router

# Импортируем наши классы и готовый объект аутентификации
from app.admin import UserAdmin, DishAdmin, OrderAdmin, authentication_backend


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Автоматическое создание таблиц при запуске приложения
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title='My_Project', lifespan=lifespan)

# Передаем authentication_backend, чтобы закрыть доступ посторонним
admin = Admin(
    app=app,
    engine=engine,
    authentication_backend=authentication_backend
)

# Регистрируем все панели в админке
admin.add_view(UserAdmin)
admin.add_view(DishAdmin)
admin.add_view(OrderAdmin)


@app.get("/")
async def read_root():
    return {"message": "Hello"}

@app.get("/mockup")
async def serve_mockup():
    mockup_path = Path(__file__).parent / "mockup.html"
    if mockup_path.exists():
        return FileResponse(mockup_path)
    return {"error": "Mockup file not found"}


# Подключаем роутеры вашего приложения
app.include_router(users_router)
app.include_router(dish_router)
app.include_router(orders_router)

@app.get("/status")
async def get_status():
    return {"status": "working"}