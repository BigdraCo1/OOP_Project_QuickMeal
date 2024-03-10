from fastapi import APIRouter, HTTPException, status
from constants.controller import system
from utils.dependencies import restaurant_dependency

app = APIRouter()


@app.delete("/{restaurant}", tags=['Delete'], status_code=status.HTTP_204_NO_CONTENT)
async def remove_restaurant(restaurant: str, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.remove_restaurant(restaurant) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no restaurant name : {restaurant}")
    


@app.get("/show_restaurant_detail/{restaurant_name}", tags = ["Restaurant"])
async def show_restaurant_detail_by_name(restaurant_name: str) -> dict:
    return system.show_restaurant_detail_by_name(restaurant_name)

@app.get("/show_request_order_list_in_restaurant/{restaurant_id}", tags = ["Restaurant"])
async def show_request_order_list_in_restaurant(restaurant_id: str) -> dict:
    return system.show_request_order_list_in_restaurant(restaurant_id)

@app.get("/show_requested_order_list_in_restaurant/{restaurant_id}", tags = ["Restaurant"])
async def show_requested_order_list_in_restaurant(restaurant_id: str) -> dict:
    return system.show_requested_order_list_in_restaurant(restaurant_id)

@app.get("/show_finished_order_list_in_restaurant/{restaurant_id}", tags = ["Restaurant"])
async def show_finished_order_list_in_restaurant(restaurant_id: str) -> dict:
    return system.show_finished_order_list_in_restaurant(restaurant_id)