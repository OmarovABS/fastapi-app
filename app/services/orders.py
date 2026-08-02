from fastapi import HTTPException
from app.schemas import OrderCreate, OrderResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, func
from app.db.models import Order, User, Dish


async def create_order(
        order_by_user: OrderCreate,
        user_telephone: str,
        user_name: str,
        db: AsyncSession
) -> Order:

    query_dish = select(Dish).where(Dish.title == order_by_user.product)
    result_dish = await db.execute(query_dish)
    dish = result_dish.scalar_one_or_none()

    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")


    query_user = select(User).where(User.telephone == user_telephone)
    result_user = await db.execute(query_user)
    user = result_user.scalar_one_or_none()


    if not user:
        user = User(
            name=user_name,
            telephone=user_telephone
        )
        db.add(user)

        await db.flush()


    new_order = Order(
        product=order_by_user.product,
        total_price=dish.price,
        user_id=user.id
    )

    db.add(new_order)


    await db.commit()
    await db.refresh(new_order)

    return new_order