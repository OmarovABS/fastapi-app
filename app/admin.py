import os
from dotenv import load_dotenv
from starlette.requests import Request
from sqladmin import ModelView
from sqladmin.authentication import AuthenticationBackend
from app.db import Dish, User, Order

# Загружаем переменные окружения
load_dotenv()

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
ADMIN_SECRET_KEY = os.getenv("ADMIN_SECRET_KEY")

# 1. БЭКЕНД АУТЕНТИФИКАЦИИ
class SimpleAdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # Проверяем данные строго из .env
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session.update({"is_admin": True})
            return True

        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return request.session.get("is_admin") is True

# Инициализируем бэкенд ключом из .env
authentication_backend = SimpleAdminAuth(secret_key=ADMIN_SECRET_KEY)


# 2. ОПРЕДЕЛЕНИЕ СТРУКТУРЫ АДМИН-ПАНЕЛИ (MODEL VIEWS)
class UserAdmin(ModelView, model=User):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "person"
    column_list = ["id", "telephone", "email"]
    column_searchable_list = ["telephone", "email"]
    form_columns = ["telephone", "email"]


class DishAdmin(ModelView, model=Dish):
    name = "Блюдо"
    name_plural = "Меню (Блюда)"
    icon = "restaurant"
    column_list = ["id", "title", "price", "category", "description"]
    column_searchable_list = ["title", "category"]
    form_columns = ["title", "price", "category", "description"]


class OrderAdmin(ModelView, model=Order):
    name = "Заказ"
    name_plural = "Заказы"
    icon = "shopping_cart"
    column_list = ["id", "product", "total_price", "user_id"]
    column_sortable_list = ["id", "total_price"]
    column_searchable_list = ["product"]
    form_columns = ["product", "total_price", "user_id"]