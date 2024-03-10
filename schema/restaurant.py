from pydantic import BaseModel
from schema.food import Food

class Restaurant_body(BaseModel):
    name_restaurant : str
    restaurant_location : str
    food: list[Food]