from pydantic import BaseModel

class add_food_api(BaseModel):
    customer_id: str
    food_id: str
    size: str
    quantity: int

class size_food_api(BaseModel):
    customer_id: str
    food_id: str
    size: str
    new_size: str

class quantity_food_api(BaseModel):
    customer_id: str
    food_id: str
    quantity: int
    size: str
    new_quantity: int

class add_address_api(BaseModel):
    customer_id: str 
    address: str
