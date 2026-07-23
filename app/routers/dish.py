from fastapi import APIRouter, Depends
from app.schemas import DishResponse
from app.services import get_dish_service, get_dish_from_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db


router = APIRouter(
    prefix='/dish',
    tags=['my_project']
)

@router.get('/', response_model=list[DishResponse])
async def get_dish(db: AsyncSession = Depends(get_db)):
    return await get_dish_service(db=db)

@router.get('/get_dish_by_category/{dish_category}', response_model=list[DishResponse])
async def get_dish_by_category(dish_category: str, db: AsyncSession = Depends(get_db)):
    return await get_dish_from_db(dish_category=dish_category, db=db)

