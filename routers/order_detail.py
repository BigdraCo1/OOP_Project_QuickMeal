from constants.controller import system
from fastapi import APIRouter, HTTPException, status


app = APIRouter()

@app.get("/show_order_detail/{order_id}", tags = ["General"])
async def show_order_detail(order_id: str) -> dict:
    return system.show_order_detail(order_id)

@app.get("/show_pocket/{account_id}", tags = ["General"])
async def show_pocket(account_id: str) -> dict:
    return system.show_pocket_detail(account_id)

@app.get("/show_payment/{account_id}", tags = ["General"])
async def show_payment(account_id: str) -> dict:
    return system.show_payment_detail(account_id)
    
