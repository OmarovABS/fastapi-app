from fastapi import APIRouter, Depends
from app.schemas import schemas
from typing import List
from app.service import busines as bs
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db

router = APIRouter(
    prefix='/users',
    tags=['my_project']
)

# 2. Добавляем async, await и меняем тип db на AsyncSession
@router.post('/create')
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await bs.create_user(user=user, db=db)

@router.get('/all')
async def all_users(db: AsyncSession = Depends(get_db)) -> List[schemas.UserResponse]:
    return await bs.all_users(db=db)

@router.delete('/clear_table')
async def clear_table(db: AsyncSession = Depends(get_db)) -> dict:
    return await bs.clear_table(db=db)

@router.get("/user_for_id/{user_id}")
async def user_for_id(user_id: int, db: AsyncSession = Depends(get_db)) -> schemas.UserResponse:
    return await bs.user_for_id(user_id=user_id, db=db)