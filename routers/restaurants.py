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