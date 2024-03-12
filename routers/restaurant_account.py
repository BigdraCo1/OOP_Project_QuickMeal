from fastapi import APIRouter, HTTPException, status
from constants.controller import system
from utils.dependencies import restaurant_dependency

app = APIRouter(tags = ["Restaurant Account"])


@app.get("/show_request_order_list_in_restaurant_account/{account_id}")
async def show_request_order_list_in_restaurant_account(account_id: str, restaurant : restaurant_dependency) -> dict:
    if restaurant is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_request_order_list_in_restaurant_account(account_id)


@app.get("/show_requested_order_list_in_restaurant_account/{account_id}")
async def show_requested_order_list_in_restaurant_account(account_id: str, restaurant : restaurant_dependency) -> dict:
    if restaurant is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_requested_order_list_in_restaurant_account(account_id)

@app.get("/show_finish_order_list_in_restaurant_account/{account_id}")
async def show_finish_order_list_in_restaurant_account(account_id: str, restaurant : restaurant_dependency) -> dict:
    if restaurant is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_finish_order_list_in_restaurant_account(account_id)

@app.get("/restaurant/account/{account_id}")
async def show_restaurant_by_restaurant_account_id(account_id: str, restaurant : restaurant_dependency) -> dict:
    if restaurant is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_restaurant_by_restaurant_account_id(account_id)

