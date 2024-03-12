from constants.controller import system
from fastapi import APIRouter, HTTPException, status
from utils.dependencies import account_dependency

app = APIRouter()


@app.get("/show/order/detail/{order_id}", tags = ["General"])
async def show_order_detail(order_id: str, acc : account_dependency) -> dict:
    if acc is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_order_detail(order_id)


@app.get("/show/pocket/{account_id}", tags = ["General"])
async def show_pocket(account_id: str, acc : account_dependency) -> dict:
    if acc is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_pocket_detail(account_id)


@app.get("/show/payment/{account_id}", tags = ["General"])
async def show_payment(account_id: str,acc : account_dependency) -> dict:
    if acc is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_payment_detail(account_id)
    
