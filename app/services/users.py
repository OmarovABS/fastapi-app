from fastapi import HTTPException
from app.schemas.users import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.db.models.users import User



async def user_create(user: UserCreate, db: AsyncSession):
    query = select(User).where(User.email==user.email)
    result = await db.execute(query)
    chek_user = result.scalar_one_or_none()
    if chek_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже имеется!")
    new_user = User(
        name = user.name.capitalize(),
        surname = user.surname.capitalize(),
        telephone = user.telephone,
        email = user.email
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

async def user_delete(user_id: str, db: AsyncSession) -> dict:
    query = select(User).where(User.id==user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь с таким id не найден!")
    await db.delete(user)
    await db.commit()
    return {"message": f"Пользователь под id: {user_id} успешно удален!"}

async def table_clear(db: AsyncSession) -> dict:
    query = select(User.name)
    result = await db.execute(query)
    total = result.scalars()
    if len(total) == 0:
        return {"message": "Таблица уже пуста!"}
    delete_query = delete(User)
    await db.execute(delete_query)
    await db.commit()
    return {"message": "Таблица успешно очищена!"}

