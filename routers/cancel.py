from constants.controller import system
from fastapi import APIRouter, HTTPException, status


app = APIRouter()

@app.post("/cancel_by_customer/{account_id}/{order_id}", tags = ["Cancel"])
async def cancel_order(account_id: str, order_id: str) -> dict:
    return {"message": system.customer_cancel_order(account_id, order_id)}


@app.post("/cancel_by_restaurant/{restaurant_account_id}/{order_id}/{food_name}/{string}", tags = ["Cancel"])
async def cancel_food(restaurant_account_id: str, order_id: str, food_name: str, string: str) -> dict:
    return  {"message": system.restaurant_cancel_order(restaurant_account_id, order_id, food_name, string)}

@app.post("/cancel_by_rider/{rider_account_id}/{order_id}", tags = ["Cancel"])
async def cancel_rider(rider_account_id: str, order_id: str) -> dict:
    return {"message": system.rider_cancel_order(rider_account_id, order_id)}
