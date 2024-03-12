from constants.controller import system
from fastapi import APIRouter, HTTPException, status
from utils.dependencies import user_dependency

app = APIRouter()

@app.put("/order/confirm/{customer_id}", tags = ["Order"])
async def confirm_order(customer_id: str, user : user_dependency) -> dict:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.confirm_customer_order(customer_id)
    }