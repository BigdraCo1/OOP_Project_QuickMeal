from constants import controller
from schema import food
from fastapi import APIRouter, HTTPException, status


app = APIRouter(prefix="/edit",
                   tags=["Editing menu"], responses={404: {"description": "Not found"}})


@app.put("/{restaurant}/{menu}", status_code=status.HTTP_202_ACCEPTED)
async def edit_menu(restaurant: str, menu: str, request: food.Food):
    return controller.system.edit_menu(restaurant, menu, request)


@app.delete("/{restaurant}/{menu}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_menu(restaurant: str, menu: str):
    if controller.system.remove_menu(restaurant, menu) != 'Removed Food from menu':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant : {restaurant} or Menu : {menu} is not found")


@app.post("/{restaurant}", status_code=status.HTTP_201_CREATED)
async def new_menu(restaurant: str, request: food.Food):
    return controller.system.new_menu(restaurant, request)