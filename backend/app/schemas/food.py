from pydantic import BaseModel


class FoodCreate(BaseModel):
    food_name: str
    calories: int


class FoodResponse(BaseModel):
    id: int
    food_name: str
    calories: int

    model_config = {"from_attributes": True}


class TextRequest(BaseModel):
    text: str
