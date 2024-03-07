from constants.controller import system
from schema import basket
from fastapi import APIRouter

app = APIRouter()

#show basket 
@app.get("/basket/{customer_id}", tags=["Basket"])
async def get_basket(customer_id: str) -> dict:
    return system.show_basket(customer_id)

#add food to basket 
@app.post("/basket/{food_id}", tags=["Basket"])
async def add_food(body: basket.add_food_api) -> str:
    return system.add_food_to_basket(body.customer_id, body.food_id, body.size, body.amount)

#add address for basket
@app.post("/basket/address", tags=["Basket"])
async def add_address(body: basket.add_address_api) -> str:
    return system.add_address_to_basket(body.customer_id, body.address)

#change amount of food in basket
@app.put("/basket/{food_id}/amount", tags=["Basket"])
async def change_amount(body: basket.amount_food_api) -> str:
    return system.change_amount(body.customer_id, body.food_id, body.amount, body.new_amount, body.size)

#change size of food in basket
@app.put("/basket/{food_id}/size", tags=["Basket"])
async def change_size(body: basket.size_food_api) -> str:
    return system.change_size(body.customer_id, body.food_id, body.size, body.new_size)
