from constants.controller import system
from fastapi import APIRouter

app = APIRouter()

#show every restaurant
@app.get("/show/restaurant", tags=["General"])
async def show_restaurant() -> dict:
    return system.show_restaurant()

#show every menu in clicked restaurant
@app.get("/menu/{restaurant_id}", tags=["General"])
async def show_restaurant_menu(restaurant_id: str) -> dict:
    return system.show_restaurant_menu(restaurant_id)

#show detail in clicked food
@app.get("/detail/{food_id}", tags=["General"])
async def food_detail(food_id: str) -> dict:
    return system.show_food_detail(food_id)