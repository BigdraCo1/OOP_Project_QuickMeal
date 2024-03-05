from pydantic import BaseModel

class add_food_api(BaseModel):
    account_id: str
    food_id: str

class add_review_api(BaseModel):
    customer_id: str 
    rating: int 
    comment: str
    order_id: str 
    restaurant_id: str

class remove_review_api(BaseModel):
    customer_id: str 
    restaurant_id: str

class show_menu_api(BaseModel):
    restaurant_name: str 

class restaurant_name(BaseModel):
    restaurant_name: str 

class show_food_detail_api(BaseModel):
    restaurant_name: str 
    food_name: str 