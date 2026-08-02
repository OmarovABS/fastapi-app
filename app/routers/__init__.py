from app.routers.users import router as users_router
from app.routers.dish import router as dish_router
from app.routers.orders import router as orders_router
#==============================================================================================
__all__ = ['users_router', 'dish_router', 'orders_router']