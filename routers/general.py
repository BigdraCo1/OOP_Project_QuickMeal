from constants.controller import system
from fastapi import APIRouter,HTTPException , status
from utils.dependencies import user_dependency, restaurant_dependency, rider_dependency

app = APIRouter()

#show every restaurant
@app.get("/show/restaurant", tags=["General"])
async def show_restaurant():
    return system.show_restaurant()

#show every menu in clicked restaurant
@app.get("/show/{restaurant_id}/menu", tags=["General"])
async def show_restaurant_menu(restaurant_id: str) -> dict:
    return system.show_restaurant_menu(restaurant_id)

#show detail in clicked food
@app.get("/show/{food_id}/detail", tags=["General"])
async def food_detail(food_id: str) -> dict:
    return system.show_food_detail(food_id)

#show account profile
@app.get("/show/profile/{account_id}", tags=["General"])
async def show_account_profile(account_id: str, user : user_dependency, restaurant_acc : restaurant_dependency, rider : rider_dependency) -> dict:
    if (user is None) and (restaurant_acc is None) and (rider is None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_account_profile(account_id)