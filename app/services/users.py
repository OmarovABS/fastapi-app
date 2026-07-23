from fastapi import HTTPException
from app.schemas import UserCreate, UserOrders, UserOrdersResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from app.db.models import User, Order
from typing import List



async def user_create(user: UserCreate, db: AsyncSession):
    query = select(User).where(User.email==user.email)
    query2 = select(User).where(User.telephone==user.telephone)
    result = await db.execute(query)
    result2 = await db.execute(query2)
    chek_user = result.scalar_one_or_none()
    chek_user2 = result2.scalar_one_or_none()
    if chek_user or chek_user2:
        raise HTTPException(status_code=400, detail="Пользователь с таким email или телефоном уже имеется!")
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

async def user_delete(user_id: int, db: AsyncSession) -> dict:
    query = select(User).where(User.id==user_id)
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь с таким id не найден!")
    await db.delete(user)
    await db.commit()
    return {"message": f"Пользователь под id: {user_id} успешно удален!"}

async def table_clear(db: AsyncSession) -> dict:
    query = select(User)
    result = await db.execute(query)
    total = result.scalars().all()
    if len(total) == 0:
        return {"message": "Таблица уже пуста!"}
    delete_query = delete(User)
    await db.execute(delete_query)
    await db.commit()
    return {"message": "Таблица успешно очищена!"}

async def get_users(db: AsyncSession):
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()


async def get_order_by_user(chek_user: UserOrders, db: AsyncSession) -> UserOrdersResponse:
    query = (
        select(Order)
        .join(Order.user)
        .where(User.telephone == chek_user.telephone,User.email == chek_user.email)
    )
    result = await db.execute(query)
    orders_by_users = result.scalars().all()
    if not orders_by_users:
        raise HTTPException(status_code=404, detail="Пользователь с таким телефоном или email не найден!")

    return UserOrdersResponse(orders=orders_by_users)