from pydantic import BaseModel


class Receipe(BaseModel):
    food_name: str
    receipe: str
    ingredients: list
    cooking_time: str
    cooking_instructions: str











