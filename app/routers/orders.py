from fastapi import APIRouter, Depends, Path
from app.schemas import OrderCreate, OrderResponse
from app.services import create_order
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db


router = APIRouter(
    prefix='/orders',
    tags=['my_project']
)
@router.post('/create_order/{user_telephone}/{user_name}', response_model=OrderResponse)
async def order_create(
    order_by_user: OrderCreate,
    user_telephone: str = Path(..., min_length=11, max_length=11),
    user_name: str = Path(..., description="User name"),
    db: AsyncSession = Depends(get_db)):
    return await create_order(order_by_user=order_by_user, user_telephone=telephone, user_name=name, db=db)