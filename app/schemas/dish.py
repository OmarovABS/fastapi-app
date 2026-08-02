from pydantic import BaseModel, Field, ConfigDict

#==============================================================================================

class DishResponse(BaseModel):
    title: str
    price: float
    category: str
    description: str

    model_config = ConfigDict(from_attributes=True)
