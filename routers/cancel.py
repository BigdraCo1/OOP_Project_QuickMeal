from databases import database
from fastapi import APIRouter, HTTPException, status


app = APIRouter()

@app.post("/cancel_order", tags = ["Orders"])
async def cancel_order(account_id: str, order_id: str) -> dict:
    return {
        "data": database.system.customer_cancel_order(account_id, order_id)
    }

@app.post("/cancel_food", tags = ["Orders"])
async def cancel_food(restaurant_account_id: str, order_id: str, food_name: str, string: str) -> dict:
    return {
        "data": database.system.restaurant_cancel_order(restaurant_account_id, order_id, food_name, string)
    }