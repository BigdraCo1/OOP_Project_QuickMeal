from databases import database
from schema import food
from fastapi import APIRouter, HTTPException, status


app = APIRouter()


@app.put("/{restaurant}/{menu}", tags=['Edit'], status_code=status.HTTP_202_ACCEPTED)
async def edit_menu(restaurant: str, menu: str, request: food.Food):
    return database.system.edit_menu(restaurant, menu, request)


@app.delete("/{restaurant}/{menu}", tags=['Delete'], status_code=status.HTTP_204_NO_CONTENT)
async def remove_menu(restaurant: str, menu: str):
    if database.system.remove_menu(restaurant, menu) != 'Removed Food from menu':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant : {restaurant} or Menu : {menu} is not found")