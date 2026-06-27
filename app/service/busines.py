from fastapi import HTTPException
from app.schemas import schemas
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.db.models import User



async def create_user(user: schemas.UserCreate, db: AsyncSession) -> dict:
    query = select(User).where(User.email == user.email)
    result = await db.execute(query)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail='Пользователь с таким email уже существует!')

    new_user = User(name=user.name, email=user.email, age=user.age)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {
        "data": "Пользователь успешно создан!",
        "user_name": new_user.name
    }


async def all_users(db: AsyncSession):
    query = select(User)
    result = await db.execute(query)
    users = result.scalars().all()
    return users


async def clear_table(db: AsyncSession) -> dict:
    query = select(User)
    result = await db.execute(query)
    users = result.scalars().all()

    if len(users) == 0:
        raise HTTPException(status_code=400, detail='Таблица уже пуста!')
    await db.execute(delete(User))
    await db.commit()

    return {"data": "Table cleared!"}


async def user_for_id(user_id: int, db: AsyncSession):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found in db!')  # Исправлен статус на 404 (Not Found)
    return user