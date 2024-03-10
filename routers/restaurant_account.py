from fastapi import APIRouter, HTTPException, status
from constants.controller import system
from utils.dependencies import restaurant_dependency

app = APIRouter()


@app.get("/show_request_order_list_in_restaurant_account/{account_id}", tags = ["Restaurant Account"])
async def show_request_order_list_in_restaurant_account(account_id: str) -> dict:
    return system.show_request_order_list_in_restaurant_account(account_id)


@app.get("/show_requested_order_list_in_restaurant_account/{account_id}", tags = ["Restaurant Account"])
async def show_requested_order_list_in_restaurant_account(account_id: str) -> dict:
    return system.show_requested_order_list_in_restaurant_account(account_id)

@app.get("/show_finish_order_list_in_restaurant_account/{account_id}", tags = ["Restaurant Account"])
async def show_finish_order_list_in_restaurant_account(account_id: str) -> dict:
    return system.show_finish_order_list_in_restaurant_account(account_id)

@app.get("/restaurant_account/{account_id}", tags = ["Restaurant Account"])
async def show_restaurant_by_restaurant_account_id(account_id: str) -> dict:
    return system.show_restaurant_by_restaurant_account_id(account_id)

