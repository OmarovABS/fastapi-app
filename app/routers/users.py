from fastapi import APIRouter, Depends
from app.schemas.users import UserCreate, UserResponse
from app.services import users as u
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db


router = APIRouter(
    prefix='/users',
    tags=['my_project']
)

@router.post('/create', response_model=UserResponse)
async def user_create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await u.user_create(user=user, db=db)

@router.delete('/delete_user/{user_id}')
async def user_delete(user_id: int, db: AsyncSession = Depends(get_db)) -> dict:
    return await u.user_delete(user_id=user_id, db=db)

@router.delete('/table_clear')
async def table_clear(db: AsyncSession=Depends(get_db)) -> dict:
    return await u.table_clear(db=db)