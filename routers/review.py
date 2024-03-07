from constants.controller import system
from schema import review
from fastapi import APIRouter

app = APIRouter()

#review
@app.get("/review/show", tags=['Review'])
async def get_restaurant_review(restaurant_id: str) -> dict:
    return system.show_review(restaurant_id)

#add review to restaurant
@app.post("/review/add", tags=["Review"])
async def add_restaurant_review(body: review.add_review_api) -> str:
    return system.add_review_to_restaurant(
        body.customer_id, body.rating, body.comment, body.restaurant_id)

#remove review from restaurant
@app.delete("/review/remove/{customer_id}", tags=["Review"])
async def remove_restaurant_review(customer_id: str ,restaurant_id: str) -> str:
    return system.remove_review_from_restaurant(customer_id, restaurant_id)
