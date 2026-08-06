from pydantic import BaseModel, ConfigDict

class AdminCreate(BaseModel):
    username: str
    password: str

class AdminResponse(BaseModel):
    username: str
    password: str
    role: str = "admin"

    model_config = ConfigDict(from_attributes=True)