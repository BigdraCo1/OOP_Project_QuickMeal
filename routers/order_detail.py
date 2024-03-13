from constants.controller import system
from fastapi import APIRouter, HTTPException, status,Depends
from typing import Annotated

app = APIRouter()


@app.get("/show/order/detail/{order_id}", tags = ["General"])
async def show_order_detail(order_id: str, acc : Annotated[dict,Depends(system.get_current_account)]) -> dict:
    if acc is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_order_detail(order_id)


@app.get("/show/pocket/{account_id}", tags = ["General"])
async def show_pocket(account_id: str, acc : Annotated[dict,Depends(system.get_current_account)]) -> dict:
    if acc is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_pocket_detail(account_id)


@app.get("/show/payment/{account_id}", tags = ["General"])
async def show_payment(account_id: str,acc : Annotated[dict,Depends(system.get_current_account)]) -> dict:
    if acc is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_payment_detail(account_id)


@app.post("/show/pocket/topup/{account_id}/{amount}", tags = ["General"])
async def topup_pocket(account_id: str, amount: int, acc: Annotated[dict,Depends(system.get_current_account)]) -> str:
    top_up = system.topup_pocket(account_id, amount)
    if top_up is None or acc is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return top_up
    
