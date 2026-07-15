from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserCreate(BaseModel):
    name: str
    surname: str
    telephone: str = Field(min_length=11, max_length=11)
    email: EmailStr

class UserResponse(BaseModel):
    name: str
    surname: str
    telephone: str = Field(min_length=11, max_length=11)

    model_config = ConfigDict(from_attributes=True)

