from constants.controller import system
from fastapi import APIRouter, HTTPException, status

app = APIRouter()

@app.put("/order/confirm/{customer_id}", tags = ["Order"])
async def confirm_order(customer_id: str) -> dict:
    return {
        "data": system.confirm_customer_order(customer_id)
    }