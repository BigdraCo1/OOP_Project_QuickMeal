from databases import database
from schema import food
from fastapi import APIRouter, HTTPException, status


app = APIRouter(tags=["Editing menu"], responses={404: {"description": "Not found"}})


@app.get("/{restaurant}", status_code=status.HTTP_200_OK)
async def menu_list(restaurant):
    if isinstance(database.system.get_menu_list(restaurant), str):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=database.system.get_menu_list(restaurant))
    return database.system.get_menu_list(restaurant)


@app.put("/{restaurant}/{menu}", status_code=status.HTTP_202_ACCEPTED)
async def edit_menu(restaurant: str, menu: str, request: food.Food):
    return database.system.edit_menu(restaurant, menu, request)


@app.delete("/{restaurant}/{menu}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_menu(restaurant: str, menu: str):
    if database.system.remove_menu(restaurant, menu) != 'Removed Food from menu':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant : {restaurant} or Menu : {menu} is not found")


@app.post("/{restaurant}", status_code=status.HTTP_201_CREATED)
async def new_menu(restaurant: str, request: food.Food):
    return database.system.new_menu(restaurant, request)