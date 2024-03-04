from databases import database
from fastapi import APIRouter, HTTPException, status


app = APIRouter()

@app.get("/show_order_detail", tags = ["Orders"])
async def show_order_detail(order_id: str, account_id: str) -> dict:
    return {
        "data": database.system.show_order_detail(order_id, account_id)
    }

@app.get("/show_pocket", tags = ["Pocket"])
async def show_pocket(account_id: str) -> dict:
    return {
        "data": database.system.show_pocket_detail(account_id)
    }

@app.get("/show_payment", tags = ["Payment"])
async def show_payment(account_id: str) -> dict:
    return {
        "data": database.system.show_payment_detail(account_id)
    }