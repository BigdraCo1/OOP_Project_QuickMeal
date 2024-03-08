from constants.controller import system
from fastapi import APIRouter

app = APIRouter()

#show every restaurant
@app.get("/show/restaurant", tags=["General"])
async def show_restaurant() -> dict:
    return system.show_restaurant()

#show every menu in clicked restaurant
@app.get("/show/{restaurant_id}/menu", tags=["General"])
async def show_restaurant_menu(restaurant_id: str) -> dict:
    return system.show_restaurant_menu(restaurant_id)

#show detail in clicked food
@app.get("/show/{food_id}/detail", tags=["General"])
async def food_detail(food_id: str) -> dict:
    return system.show_food_detail(food_id)