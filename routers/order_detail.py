from databases import database
from fastapi import APIRouter, HTTPException, status


app = APIRouter()

@app.get("/get_order_state", tags = ["Orders"])
async def get_order_state(account_id: str) -> dict:
    return {
        "data": database.system.get_account_order_state(account_id)
    }

@app.get("/get_payment", tags = ["Orders"])
async def get_payment(account_id: str) -> dict:
    return {
        "data": database.system.get_account_payment_status(account_id)
    }

@app.get("/show_order_detail", tags = ["Orders"])
async def show_order_detail(order_id: str, account_id: str) -> dict:
    return {
        "data": database.system.show_order_detail(order_id, account_id)
    }