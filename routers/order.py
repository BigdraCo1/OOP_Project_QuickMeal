from constants.controller import system
from fastapi import APIRouter, HTTPException, status

app = APIRouter()

@app.put("/{customer_id}/{order_id}", tags = ["Orders"])
async def confirm_order(customer_id: str, order_id: str) -> dict:
    return {
        "data": system.confirm_customer_order(customer_id, order_id)
    }