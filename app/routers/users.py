from fastapi import APIRouter, Depends
from app.schemas import UserCreate, UserResponse, UserOrders, UserOrdersResponse
from app.services import user_delete, table_clear, get_users, get_order_by_user
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from typing import List
from app.security_by_admin import security


#==============================================================================================

router = APIRouter(
    prefix='/users'
)

#==============================================================================================

@router.get('/', response_model=list[UserResponse],
summary="Получение списка всех пользователей (ТОЛЬКО ДЛЯ АДМИНА)",
tags=["Users"], dependencies=[Depends(security.access_token_required)])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db=db)

#==============================================================================================

@router.delete('/delete_user/{user_id}',
summary="Удаление пользователя по id (ТОЛЬКО ДЛЯ АДМИНА)",
tags=["Users"], dependencies=[Depends(security.access_token_required)])
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    return await user_delete(user_id=user_id, db=db)

#==============================================================================================

@router.delete('/table_clear',
summary="Очистка таблицы (ТОЛЬКО ДЛЯ АДМИНА)",
tags=["Users"], dependencies=[Depends(security.access_token_required)])
async def clear_table(db: AsyncSession=Depends(get_db)) -> dict:
    return await table_clear(db=db)

#==============================================================================================

@router.post('/get_order_by_user',
summary="Получение заказов по пользователю",
tags=["Users"])
async def get_orders(cheсk_user: UserOrders, db: AsyncSession = Depends(get_db)) -> UserOrdersResponse:
    return await get_order_by_user(cheсk_user=cheсk_user, db=db)
