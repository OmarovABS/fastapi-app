from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqladmin import Admin
from pathlib import Path
from app.db import Base, engine
from app.routers import users_router, dish_router, orders_router
from app.admin import UserAdmin, DishAdmin, OrderAdmin, authentication_backend
from fastapi import HTTPException, Response, Depends
from authx import AuthX, AuthXConfig
from app.schemas import AdminCreate
from app.security_by_admin import security, config
import os
from dotenv import load_dotenv

load_dotenv()
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
ADMIN_SECRET_KEY = os.getenv("ADMIN_SECRET_KEY")

#==============================================================================================

@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

#==============================================================================================

app = FastAPI(title='My_Project', lifespan=lifespan,
swagger_ui_parameters={"defaultModelsExpandDepth": -1})

#==============================================================================================

admin = Admin(
    app=app,
    engine=engine,
    authentication_backend=authentication_backend
)
admin.add_view(UserAdmin)
admin.add_view(DishAdmin)
admin.add_view(OrderAdmin)


#==============================================================================================

@app.get("/", tags=["Home page"], summary="Начальная страница")
async def read_root():
    return {"message": "Hello"}

#==============================================================================================

app.include_router(users_router)
app.include_router(dish_router)
app.include_router(orders_router)

#==============================================================================================

@app.get("/status", tags=["Project status"], summary="Узнать статус проекта")
async def get_status():
    return {"status": "working"}

#==============================================================================================


@app.post("/login_by_admin", tags=["Login by Admin"], summary="Проверка на Админа")
async def login_by_admin(creds: AdminCreate, response: Response):
    if creds.username == ADMIN_USERNAME and creds.password == ADMIN_PASSWORD:
        token = security.create_access_token(uid="1")
        response.set_cookie(config.JWT_ACCESS_COOKIE_NAME, token)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")