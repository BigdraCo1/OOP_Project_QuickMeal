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
    
