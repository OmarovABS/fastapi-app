from fastapi import HTTPException
from app.schemas import DishResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, func
from app.db.models import Dish

#==============================================================================================

async def get_dish_service(db: AsyncSession):
    query = select(Dish)
    result = await db.execute(query)
    return result.scalars().all()

#==============================================================================================

async def get_dish_from_db(dish_category: str, db: AsyncSession):
    query = select(Dish).where(Dish.category == dish_category.capitalize())
    result = await db.execute(query)
    dishes = result.scalars().all()
    if not dishes:
        raise HTTPException(status_code=404, detail="Блюда с такой категорией не найдены!")
    return dishes

