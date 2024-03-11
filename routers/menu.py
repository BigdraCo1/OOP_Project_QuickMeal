from constants.controller import system
from schema import food
from fastapi import APIRouter, HTTPException, status
from utils.dependencies import restaurant_dependency

app = APIRouter(tags=["Editing menu"], responses={404: {"description": "Not found"}})


@app.get("/{restaurant}", status_code=status.HTTP_200_OK)
async def menu_list(restaurant: str, restaurant_dep: restaurant_dependency):
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if isinstance(system.get_menu_list(restaurant), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=system.get_menu_list(restaurant))
    return system.get_menu_list(restaurant)


@app.get("/{restaurant}/{menu}", status_code=status.HTTP_200_OK)
async def menu_list(restaurant: str, menu: str, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if isinstance(system.get_menu(restaurant, menu), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=system.get_menu_list(restaurant))
    return system.get_menu(restaurant, menu)


@app.put("/{restaurant}/{menu}", status_code=status.HTTP_202_ACCEPTED)
async def edit_menu(restaurant: str, menu: str, request: food.Food, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.edit_menu(restaurant, menu, request)


@app.delete("/{restaurant}/{menu}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_menu(restaurant: str, menu: str, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.remove_menu(restaurant, menu) != 'Removed Food from menu':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant : {restaurant} or Menu : {menu} is not found")


@app.post("/{restaurant}", status_code=status.HTTP_201_CREATED)
async def new_menu(restaurant: str, request: food.Food, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.new_menu(restaurant, request)