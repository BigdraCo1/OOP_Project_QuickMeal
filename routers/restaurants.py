from fastapi import APIRouter, HTTPException, status
from constants.controller import system
from schema.restaurant import Restaurant_body
from utils.dependencies import restaurant_dependency

app = APIRouter(prefix='/restaurant_owner', tags=['Edit restaurant'])


@app.post("/")
async def add_restaurant(request: Restaurant_body, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.new_restaurant(restaurant_dep["username"] , request) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return 'Success'

@app.delete("/{restaurant}",  status_code=status.HTTP_204_NO_CONTENT)
async def remove_restaurant(restaurant: str, restaurant_dep : restaurant_dependency):
    if restaurant_dep is None or not system.check_access_by_username(restaurant_dep["username"], restaurant):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if system.remove_restaurant(restaurant) != 'Success':
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"There is no restaurant name : {restaurant}")