from constants.controller import system
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

app = APIRouter(tags=["Cancel"])


@app.post("/cancel_by_customer/{account_id}/{order_id}")
async def cancel_order(account_id: str, order_id: str, user: Annotated[dict, Depends(system.get_current_customer)]) -> dict:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"message": system.customer_cancel_order(account_id, order_id)}


@app.post("/cancel_by_restaurant/{restaurant_id}/{order_id}/{food_name}")
async def cancel_food(restaurant_id: str, order_id: str, food_name: str, restaurant: Annotated[dict,Depends(system.get_current_restaurant)]) -> dict:
    if restaurant is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"message": system.restaurant_cancel_order(restaurant_id, order_id, food_name)}


@app.post("/cancel_by_rider/{rider_account_id}/{order_id}")
async def cancel_rider(rider_account_id: str, order_id: str, rider: Annotated[dict,Depends(system.get_current_rider)]) -> dict:
    if rider is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {"message": system.rider_cancel_order(rider_account_id, order_id)}
