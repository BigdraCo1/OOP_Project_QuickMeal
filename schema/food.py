from pydantic import BaseModel


class Food(BaseModel):
    name: str
    type: str
    size: dict
    price: int
