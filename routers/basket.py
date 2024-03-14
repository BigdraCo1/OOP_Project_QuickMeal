from constants.controller import system
from schema import basket
from fastapi import APIRouter, HTTPException, status, Depends
from typing import Annotated

app = APIRouter(prefix='/basket', tags=["Basket"])


#show basket
@app.get("/custom/{customer_id}")
async def get_basket(customer_id: str, user : Annotated[dict, Depends(system.get_current_customer)]) -> dict:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_basket(customer_id)


#show address
@app.get("/address/{customer_id}")
async def show_address(customer_id: str, user: Annotated[dict, Depends(system.get_current_customer)]) -> list:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.show_address(customer_id)


#add food to basket
@app.post("/add/food")
async def add_food(body: basket.add_food_api, user: Annotated[dict, Depends(system.get_current_customer)]) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.add_food_to_basket(body.customer_id, body.food_id, body.size, body.quantity)


#add address for basket
@app.post("/add/address")
async def add_address(body: basket.add_address_api, user: Annotated[dict, Depends(system.get_current_customer)]) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.add_address_to_basket(body.customer_id, body.address)


#delete address
@app.delete("/delete/address")
async def add_address(customer_id:str, address:str, user : user_dependency) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.delete_address(customer_id, address)


#change quantity of food in basket
@app.put("/food/quantity")
async def change_quantity(body: basket.quantity_food_api, user: Annotated[dict, Depends(system.get_current_customer)]) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.change_quantity(body.customer_id, body.food_id, body.quantity, body.new_quantity, body.size)


#change size of food in basket
@app.put("/food/size")
async def change_size(body: basket.size_food_api, user: Annotated[dict, Depends(system.get_current_customer)]) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.change_size(body.customer_id, body.food_id, body.size, body.new_size)


#delete address
@app.delete("/delete/address/{customer_id}/{address}")
async def add_address(customer_id:str, address:str, user: Annotated[dict, Depends(system.get_current_customer)]) -> str:
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return system.delete_address(customer_id, address)