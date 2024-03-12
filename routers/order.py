from constants.controller import system
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

app = APIRouter()

@app.put("/order/confirm/{customer_id}", tags = ["Order"])
async def confirm_order(customer_id: str, user : Annotated[dict, Depends(system.get_current_customer)]) -> dict:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return {
        "data": system.confirm_customer_order(customer_id)
    }