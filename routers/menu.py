from ..schema.food import Food
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.put("/{restaurant}/{menu}", tags=['Edit'], status_code=status.HTTP_202_ACCEPTED)
async def edit_menu(restaurant: str, menu: str, request: Food):
    return system_controller.edit_menu(restaurant, menu, request)


@app.delete("/{restaurant}/{menu}", tags=['Delete'], status_code=status.HTTP_204_NO_CONTENT)
async def remove_menu(restaurant: str, menu: str):
    if system_controller.remove_menu(restaurant, menu) != 'Removed Food from menu':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Restaurant : {restaurant} or Menu : {menu} is not found")