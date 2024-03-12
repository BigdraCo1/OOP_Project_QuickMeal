from constants.controller import system
from schema import review
from fastapi import APIRouter, HTTPException, status,Depends
from typing import Annotated

app = APIRouter(prefix='/review', tags=['Review'])

#review
@app.get("/show/{restaurant_id}")
async def get_restaurant_review(restaurant_id: str) -> dict:
    return system.show_review(restaurant_id)


#add review to restaurant
@app.post("/add")
async def add_restaurant_review(body: review.add_review_api, user : Annotated[dict,Depends(system.get_current_customer)]) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.add_review_to_restaurant(
        body.customer_id, body.rating, body.comment, body.restaurant_id)


#remove review from restaurant
@app.delete("/remove/{customer_id}")
async def remove_restaurant_review(customer_id: str ,restaurant_id: str, user : Annotated[dict,Depends(system.get_current_customer)]) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.remove_review_from_restaurant(customer_id, restaurant_id)
