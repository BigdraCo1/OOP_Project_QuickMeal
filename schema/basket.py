from pydantic import BaseModel

class add_food_api(BaseModel):
    customer_id: str
    food_id: str
    size: str
    amount: int

class size_food_api(BaseModel):
    customer_id: str
    food_id: str
    size: str
    new_size: str

class amount_food_api(BaseModel):
    customer_id: str
    food_id: str
    amount: str
    size: str
    new_amount: str

class add_address_api(BaseModel):
    customer_id: str 
    address: str