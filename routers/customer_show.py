from constants.controller import system
from fastapi import APIRouter, HTTPException, status
from utils.dependencies import user_dependency

app = APIRouter()

@app.get("/show/current_order/{customer_id}", tags = ["Customer"])
async def show_current_order(customer_id: str, user : user_dependency) -> dict:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.show_current_order(customer_id)
        }

@app.get("/show/order_list/{customer_id}", tags = ["Customer"])
async def show_order_list(customer_id: str, user : user_dependency) -> dict:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.show_order_list(customer_id)
        }