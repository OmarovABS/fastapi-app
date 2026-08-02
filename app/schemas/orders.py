from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

#==============================================================================================

class OrderCreate(BaseModel):
    product: str = Field(..., description="Product name")

#==============================================================================================

class OrderResponse(BaseModel):
    id: int
    product: str
    total_price: Decimal  # Название и тип совпадают с вашей моделью Order
    user_id: int

    model_config = ConfigDict(from_attributes=True)