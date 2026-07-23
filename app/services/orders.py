from fastapi import HTTPException
from app.schemas import OrderCreate, OrderResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, func
from app.db.models import Order, User, Dish


async def create_order(order_by_user: OrderCreate, telephone: str, name: str,
db: AsyncSession) -> Order:

    query = select(Dish).where(Dish.title == order_by_user.product)
    result = await db.execute(query)
    dish = result.scalar_one_or_none()

    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")




    new_order = Order(
        product=order_by_user.product,
        total_price=dish.price,
        user_id=user.id
    )

    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)

    return new_order