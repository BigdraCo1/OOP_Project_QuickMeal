from fastapi import APIRouter, HTTPException, status
from constants.controller import system
from utils.dependencies import restaurant_dependency
from schema.restaurant import Restaurant_body

app = APIRouter(prefix='/restaurant', tags = ["Restaurant"])


@app.delete("/{restaurant}",  status_code=status.HTTP_204_NO_CONTENT)
async def remove_restaurant(restaurant: str, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.remove_restaurant(restaurant) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no restaurant name : {restaurant}")


@app.get("/show_restaurant_detail_by_name/{restaurant_name}")
async def show_restaurant_detail_by_name(restaurant_name: str, restaurant_dep : restaurant_dependency) -> dict:
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant_name):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_restaurant_detail_by_name(restaurant_name)


@app.get("/show_restaurant_detail_by_id/{restaurant_id}")
async def show_restaurant_detail_by_id(restaurant_id: str) -> dict:
    return system.show_restaurant_detail_by_id(restaurant_id)


@app.get("/show_request_order_list_in_restaurant/{restaurant_id}")
async def show_request_order_list_in_restaurant(restaurant_id: str, restaurant_dep : restaurant_dependency) -> dict:
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_request_order_list_in_restaurant(restaurant_id)


@app.get("/show_requested_order_list_in_restaurant/{restaurant_id}")
async def show_requested_order_list_in_restaurant(restaurant_id: str, restaurant_dep : restaurant_dependency) -> dict:
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_requested_order_list_in_restaurant(restaurant_id)


@app.get("/show_finished_order_list_in_restaurant/{restaurant_id}")
async def show_finished_order_list_in_restaurant(restaurant_id: str, restaurant_dep : restaurant_dependency) -> dict:
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_finished_order_list_in_restaurant(restaurant_id)


@app.post("/")
async def add_restaurant(request: Restaurant_body, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.new_restaurant(restaurant_dep["username"] , request) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return { 'detail' : 'Success'}


@app.get("/show_food_in_order/{order_id}")
async def show_food_in_order(order_id: str, restaurant_dep : restaurant_dependency) -> dict:
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_food_in_order(order_id)