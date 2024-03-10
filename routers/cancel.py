from constants.controller import system
from fastapi import APIRouter, HTTPException, status
from utils.dependencies import user_dependency, restaurant_dependency, rider_dependency

app = APIRouter( tags = ["Cancel"])

@app.post("/cancel_by_customer/{account_id}/{order_id}")
async def cancel_order(account_id: str, order_id: str, user : user_dependency) -> dict:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"message": system.customer_cancel_order(account_id, order_id)}


@app.post("/cancel_by_restaurant/{restaurant_account_id}/{order_id}/{food_name}/{string}")
async def cancel_food(restaurant_account_id: str, order_id: str, food_name: str, string: str, restaurant : restaurant_dependency) -> dict:
    if restaurant is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return  {"message": system.restaurant_cancel_order(restaurant_account_id, order_id, food_name, string)}

@app.post("/cancel_by_rider/{rider_account_id}/{order_id}")
async def cancel_rider(rider_account_id: str, order_id: str, rider : rider_dependency) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"message": system.rider_cancel_order(rider_account_id, order_id)}
