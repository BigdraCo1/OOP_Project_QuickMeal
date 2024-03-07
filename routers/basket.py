from constants.controller import system
from schema import basket
from fastapi import APIRouter

app = APIRouter()

#show basket 
@app.get("/basket/{customer_id}", tags=["Basket"])
async def get_basket(customer_id: str) -> dict:
    return system.show_basket(customer_id)

#show address 
@app.get("/basket/address/{customer_id}", tags=["Basket"])
async def show_address(customer_id: str) -> list:
    return system.show_address(customer_id)

#add food to basket 
@app.post("/basket/add/{food_id}", tags=["Basket"])
async def add_food(body: basket.add_food_api) -> str:
    return system.add_food_to_basket(body.customer_id, body.food_id, body.size, body.quantity)

#add address for basket
@app.post("/basket/{body.customer_id}/address", tags=["Basket"])
async def add_address(body: basket.add_address_api) -> str:
    return system.add_address_to_basket(body.customer_id, body.address)

#change quantity of food in basket
@app.put("/basket/{food_id}/quantity", tags=["Basket"])
async def change_quantity(body: basket.quantity_food_api) -> str:
    return system.change_quantity(body.customer_id, body.food_id, body.quantity, body.new_quantity, body.size)

#change size of food in basket
@app.put("/basket/{food_id}/size", tags=["Basket"])
async def change_size(body: basket.size_food_api) -> str:
    return system.change_size(body.customer_id, body.food_id, body.size, body.new_size)