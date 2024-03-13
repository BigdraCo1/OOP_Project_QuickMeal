from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated
from constants.controller import system
from schema.restaurant import Restaurant_body

app = APIRouter(prefix='/restaurant', tags = ["Restaurant"])


@app.delete("/delete/{restaurant}",  status_code=status.HTTP_204_NO_CONTENT)
async def remove_restaurant(restaurant: str, restaurant_dep : Annotated[dict, Depends(system.get_current_restaurant)]):
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_name(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.remove_restaurant(restaurant) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no restaurant name : {restaurant}")


@app.get("/show_restaurant_detail_by_name/{restaurant_name}")
async def show_restaurant_detail_by_name(restaurant_name: str, restaurant_dep : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_name(restaurant_dep["username"], restaurant_name):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_restaurant_detail_by_name(restaurant_name)


@app.get("/show_restaurant_detail_by_id/{restaurant_id}")
async def show_restaurant_detail_by_id(restaurant_id: str) -> dict:
    return system.show_restaurant_detail_by_id(restaurant_id)


@app.get("/show_request_order_list_in_restaurant/{restaurant_id}")
async def show_request_order_list_in_restaurant(restaurant_id: str, restaurant_dep : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_id(restaurant_dep["username"], restaurant_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_request_order_list_in_restaurant(restaurant_id)


@app.get("/show_requested_order_list_in_restaurant/{restaurant_id}")
async def show_requested_order_list_in_restaurant(restaurant_id: str, restaurant_dep : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_id(restaurant_dep["username"], restaurant_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_requested_order_list_in_restaurant(restaurant_id)


@app.get("/show_finished_order_list_in_restaurant/{restaurant_id}")
async def show_finished_order_list_in_restaurant(restaurant_id: str, restaurant_dep : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant_dep is None or not system.check_access_restaurant_by_restaurant_id(restaurant_dep["username"], restaurant_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_finished_order_list_in_restaurant(restaurant_id)


@app.post("/")
async def add_restaurant(request: Restaurant_body, restaurant_dep : Annotated[dict, Depends(system.get_current_restaurant)]):
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.new_restaurant(restaurant_dep["username"] , request) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return { 'detail' : 'Success'}


@app.get("/show_food_in_order/{order_id}")
async def show_food_in_order(order_id: str, restaurant_dep : Annotated[dict, Depends(system.get_current_restaurant)]) -> dict:
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_food_in_order(order_id)


@app.get("/get_restaurant_owner_id_by_restaurant_name/{restaurant_name}")
async def get_restaurant_owner_id_by_restaurant_name(restaurant_name: str) -> dict:
    return system.get_restaurant_owner_id_by_restaurant_name(restaurant_name)