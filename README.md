# My FastAPI Project

## Описание
FastAPI проект с базой данных PostgreSQL.

## Структура проекта
```
my_fastapi_proect/
├── app/
│   ├── db/              # База данных
│   │   ├── models/      # SQLAlchemy модели
│   │   └── database.py  # Настройки БД
│   ├── routers/         # API роутеры
│   ├── schemas/         # Pydantic схемы
│   └── services/        # Бизнес-логика
├── tests/               # Тесты
├── main.py              # Точка входа
├── requirements.txt     # Зависимости
└── .env.example         # Пример переменных окружения
```

## Установка
1. Клонировать репозиторий
2. Создать виртуальное окружение: `python -m venv .venv`
3. Активировать: `.venv\Scripts\activate` (Windows)
4. Установить зависимости: `pip install -r requirements.txt`
5. Создать файл `.env` на основе `.env.example`
6. Запустить: `uvicorn main:app --reload`

## API Endpoints
- `POST /users/create` - Создать пользователя
- `DELETE /users/delete_user/{user_id}` - Удалить пользователя
- `DELETE /users/table_clear` - Очистить таблицу пользователей

## Модели БД
- **User**: id, name, surname, telephone, email
- **Dish**: id, title, price, category
