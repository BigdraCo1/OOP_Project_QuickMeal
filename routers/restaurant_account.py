from fastapi import APIRouter,Depends, HTTPException, status
from constants.controller import system
from typing import Annotated

app = APIRouter(tags = ["Restaurant Account"])


@app.get("/show_request_order_list_in_restaurant_account/{account_id}")
async def show_request_order_list_in_restaurant_account(account_id: str, restaurant : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_request_order_list_in_restaurant_account(account_id)




