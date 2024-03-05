from databases import database
from fastapi import APIRouter, HTTPException, status


app = APIRouter()

@app.post("/cancel_by_customer", tags = ["Cancel"])
async def cancel_order(account_id: str, order_id: str) -> dict:
    return {
        "data": database.system.customer_cancel_order(account_id, order_id)
    }

@app.post("/cancel_by_restaurant", tags = ["Cancel"])
async def cancel_food(restaurant_account_id: str, order_id: str, food_name: str, string: str) -> dict:
    return {
        "data": database.system.restaurant_cancel_order(restaurant_account_id, order_id, food_name, string)
    }

@app.post("/cancel_by_rider", tags = ["Cancel"])
async def cancel_rider(rider_account_id: str, order_id: str) -> dict:
    return {
        "data": database.system.rider_cancel_order(rider_account_id, order_id)
    }