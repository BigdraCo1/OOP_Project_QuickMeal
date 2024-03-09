from constants.controller import system
from fastapi import APIRouter, HTTPException, status


app = APIRouter()

@app.get("/show/current_order/{customer_id}", tags = ["Customer"])
async def show_current_order(customer_id: str) -> dict:
    return {
        "data": system.show_current_order(customer_id)
        }

@app.get("/show/order_list/{customer_id}", tags = ["Customer"])
async def show_order_list(customer_id: str) -> dict:
    return {
        "data": system.show_order_list(customer_id)
        }