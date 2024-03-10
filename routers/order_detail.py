from constants.controller import system
from fastapi import APIRouter, HTTPException, status
from utils.dependencies import user_dependency, restaurant_dependency, rider_dependency

app = APIRouter()

@app.get("/show_order_detail/{order_id}", tags = ["General"])
async def show_order_detail(order_id: str, user : user_dependency, restaurant : restaurant_dependency
                            , rider: rider_dependency) -> dict:
    if (user is None) and (restaurant is None) and (rider is None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_order_detail(order_id)

@app.get("/show_pocket/{account_id}", tags = ["General"])
async def show_pocket(account_id: str, user : user_dependency, restaurant : restaurant_dependency
                            , rider: rider_dependency) -> dict:
    if (user is None) and (restaurant is None) and (rider is None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_pocket_detail(account_id)

@app.get("/show_payment/{account_id}", tags = ["General"])
async def show_payment(account_id: str, user : user_dependency, restaurant : restaurant_dependency
                            , rider: rider_dependency) -> dict:
    if (user is None) and (restaurant is None) and (rider is None):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_payment_detail(account_id)
    
