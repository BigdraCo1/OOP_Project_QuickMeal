from pydantic import BaseModel

class add_review_api(BaseModel):
    customer_id: str 
    rating: int 
    comment: str
    restaurant_id: str