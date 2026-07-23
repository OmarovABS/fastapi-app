from fastapi import APIRouter, Depends
from app.schemas import UserCreate, UserResponse, UserOrders, UserOrdersResponse
from app.services import user_create, user_delete, table_clear, get_users, get_order_by_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from typing import List

router = APIRouter(
    prefix='/users',
    tags=['my_project']
)

@router.post('/create', response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_create(user=user, db=db)

@router.get('/', response_model=list[UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db=db)

@router.delete('/delete_user/{user_id}')
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    return await user_delete(user_id=user_id, db=db)

@router.delete('/table_clear')
async def clear_table(db: AsyncSession=Depends(get_db)) -> dict:
    return await table_clear(db=db)

@router.post('/get_order_by_user')
async def get_orders(chek_user: UserOrders, db: AsyncSession = Depends(get_db)) -> UserOrdersResponse:
    return await get_order_by_user(chek_user=chek_user, db=db)
