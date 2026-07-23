# My FastAPI Project

## Описание
FastAPI проект для управления рестораном с базой данных PostgreSQL. Проект включает в себя управление пользователями, меню блюд и заказами, а также админ-панель для администрирования данных.

## Возможности
- **Управление пользователями**: создание, удаление, получение списка пользователей
- **Управление меню**: просмотр всех блюд, фильтрация по категории
- **Управление заказами**: создание заказов с привязкой к пользователям
- **Админ-панель**: веб-интерфейс для управления данными (пользователи, блюда, заказы)
- **Асинхронная работа с БД**: использование SQLAlchemy с asyncpg
- **Docker-поддержка**: готовая конфигурация для контейнеризации

## Технологический стек
- **FastAPI** - современный веб-фреймворк
- **SQLAlchemy** - ORM для работы с базой данных
- **PostgreSQL** - реляционная база данных
- **SQLAdmin** - админ-панель для FastAPI
- **Pydantic** - валидация данных
- **Docker & Docker Compose** - контейнеризация
- **Uvicorn** - ASGI сервер

## Структура проекта
```
my_fastapi_proect/
├── app/
│   ├── db/
│   │   ├── models/          # SQLAlchemy модели (User, Dish, Order)
│   │   └── database.py      # Настройки подключения к БД
│   ├── routers/             # API роутеры
│   │   ├── users.py         # Эндпоинты пользователей
│   │   ├── dish.py          # Эндпоинты блюд
│   │   └── orders.py        # Эндпоинты заказов
│   ├── schemas/             # Pydantic схемы для валидации
│   ├── services/            # Бизнес-логика
│   └── admin.py             # Настройка админ-панели
├── main.py                  # Точка входа приложения
├── requirements.txt         # Зависимости Python
├── Dockerfile               # Конфигурация Docker
├── docker-compose.yml       # Docker Compose конфигурация
├── .env.example             # Пример переменных окружения
└── .gitignore               # Игнорируемые файлы
```

## Установка и запуск

### Локальная установка

1. **Клонировать репозиторий**
   ```bash
   git clone <repository-url>
   cd my_fastapi_proect
   ```

2. **Создать виртуальное окружение**
   ```bash
   python -m venv .venv
   ```

3. **Активировать виртуальное окружение**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source .venv/bin/activate
     ```

4. **Установить зависимости**
   ```bash
   pip install -r requirements.txt
   ```

5. **Настроить переменные окружения**
   - Создать файл `.env` на основе `.env.example`
   - Заполнить необходимые параметры:
     ```env
     DATABASE_URL=postgresql+asyncpg://USER:PASSWORD@localhost:5432/DB_NAME
     ADMIN_USERNAME=your_admin_username
     ADMIN_PASSWORD=your_admin_password
     ADMIN_SECRET_KEY=your_secret_key
     ```

6. **Запустить приложение**
   ```bash
   uvicorn main:app --reload
   ```

   Приложение будет доступно по адресу: `http://localhost:8000`

### Запуск с Docker

1. **Настроить переменные окружения** в файле `.env`

2. **Запустить контейнеры**
   ```bash
   docker-compose up --build
   ```

3. **Приложение будет доступно по адресу**: `http://localhost:8000`
   **База данных**: `localhost:5432`

## API Endpoints

### Пользователи (`/users`)
- `POST /users/create` - Создать нового пользователя
- `GET /users/` - Получить список всех пользователей
- `DELETE /users/delete_user/{user_id}` - Удалить пользователя по ID
- `DELETE /users/table_clear` - Очистить таблицу пользователей
- `POST /users/get_order_by_user` - Получить заказы пользователя

### Блюда (`/dish`)
- `GET /dish/` - Получить список всех блюд
- `GET /dish/get_dish_by_category/{dish_category}` - Получить блюда по категории

### Заказы (`/orders`)
- `POST /orders/create_order/{user_telephone}/{user_name}` - Создать новый заказ

### Документация API
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Админ-панель
- **URL**: `http://localhost:8000/admin`
- **Авторизация**: используйте credentials из `.env` (ADMIN_USERNAME, ADMIN_PASSWORD)

## Модели базы данных

### User
- `id` - уникальный идентификатор
- `name` - имя пользователя
- `surname` - фамилия пользователя
- `telephone` - номер телефона
- `email` - email адрес

### Dish
- `id` - уникальный идентификатор
- `title` - название блюда
- `price` - цена
- `category` - категория блюда
- `description` - описание блюда

### Order
- `id` - уникальный идентификатор
- `product` - список продуктов в заказе
- `total_price` - общая стоимость заказа
- `user_id` - ID пользователя (внешний ключ)

## Переменные окружения

| Переменная | Описание | Пример |
|------------|----------|--------|
| `DATABASE_URL` | Строка подключения к PostgreSQL | `postgresql+asyncpg://user:password@localhost:5432/dbname` |
| `POSTGRES_USER` | Имя пользователя PostgreSQL | `postgres` |
| `POSTGRES_PASSWORD` | Пароль PostgreSQL | `password` |
| `POSTGRES_DB` | Имя базы данных | `mydb` |
| `ADMIN_USERNAME` | Логин для админ-панели | `admin` |
| `ADMIN_PASSWORD` | Пароль для админ-панели | `admin123` |
| `ADMIN_SECRET_KEY` | Секретный ключ для сессий | `your-secret-key` |

## Разработка

### Добавление новых роутеров
1. Создайте файл в `app/routers/`
2. Определите `APIRouter` с нужными эндпоинтами
3. Зарегистрируйте роутер в `main.py`:
   ```python
   app.include_router(your_router)
   ```

### Добавление новых моделей
1. Создайте модель в `app/db/models/`
2. Импортируйте её в `app/db/models/__init__.py`
3. Добавьте соответствующую Admin View в `app/admin.py`

## Лицензия
MIT License
