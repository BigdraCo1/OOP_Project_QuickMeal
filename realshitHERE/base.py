from pydantic import BaseModel

class add_food_api(BaseModel):
    customer_id: str
    food_id: str
    size: str
    amount: int

class change_amount_api(BaseModel):
    customer_id: str
    food_id: str
    amount: int

class change_size_api(BaseModel):
    customer_id: str
    food_id: str
    size: str

class add_review_api(BaseModel):
    customer_id: str 
    rating: int 
    comment: str
    order_id: str 
    restaurant_id: str

class add_address_api(BaseModel):
    customer_id: str 
    address: str