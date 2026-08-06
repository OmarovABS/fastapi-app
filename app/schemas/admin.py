from pydantic import BaseModel

class AdminCreate(BaseModel):
    username: str
    password: str

class AdminResponse(BaseModel):
    username: str
    password: str
    role: str = "admin"

    class Config:
        from_attributes = True