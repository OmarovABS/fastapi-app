from pydantic import BaseModel, Field, EmailStr, ConfigDict
from app.schemas.orders import OrderResponse

class UserCreate(BaseModel):
    name: str
    telephone: str = Field(min_length=11, max_length=11)


class UserResponse(BaseModel):
    name: str
    telephone: str = Field(min_length=11, max_length=11)

    model_config = ConfigDict(from_attributes=True)


class UserOrders(BaseModel):
    name: str
    telephone: str = Field(min_length=11, max_length=11)


class UserOrdersResponse(BaseModel):
    orders: list[OrderResponse]

    model_config = ConfigDict(from_attributes=True)