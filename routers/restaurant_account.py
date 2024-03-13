from fastapi import APIRouter,Depends, HTTPException, status
from constants.controller import system
from typing import Annotated

app = APIRouter(tags = ["Restaurant Account"])


@app.get("/show_request_order_list_in_restaurant_account/{account_id}")
async def show_request_order_list_in_restaurant_account(account_id: str, restaurant : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant is None or not system.check_access_restaurant_acc_by_id(restaurant["id"], account_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_request_order_list_in_restaurant_account(account_id)


@app.get("/restaurant/account/{account_id}")
async def show_restaurant_by_restaurant_account_id(account_id: str, restaurant: Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant is None or not system.check_access_restaurant_acc_by_id(restaurant["id"], account_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_restaurant_by_restaurant_account_id(account_id)

