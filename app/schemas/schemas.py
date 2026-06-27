from pydantic import BaseModel, Field, EmailStr



class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int =  Field(gt=0, lt=120)

class UserResponse(BaseModel):
    name: str
    age: int
    id: int

    class Config:
        from_attributes = True