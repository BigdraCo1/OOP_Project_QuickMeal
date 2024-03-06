from databases import database
import base

from fastapi import FastAPI
import uvicorn

app = FastAPI()

#show every restaurant
@app.get("/show/restaurant", tags=["Show"])
async def show_restaurant() -> dict:
    return system.show_restaurant()

#show every menu in clicked restaurant
@app.get("/menu/{restaurant_id}", tags=["Show"])
async def restaurant_menu(restaurant_id: str) -> dict:
    return system.show_restaurant_menu(restaurant_id)

#show detail in clicked food
@app.get("/show/{food_id}", tags=["Show"])
async def food_detail(food_id: str) -> dict:
    return system.show_food_detail(food_id)

#add food to basket 
@app.post("/show/{food_id}", tags=["Basket"])
async def add_food(body: base.add_food_api) -> str:
    return system.add_food_to_basket(body.customer_id, body.food_id, body.size, body.amount)

#basket 
@app.get("/basket", tags=["Basket"])
async def get_basket(customer_id: str) -> dict:
    return system.show_basket(customer_id)

#select address for basket
@app.post("/basket/address", tags=["Basket"])
async def add_address(body: base.add_address_api) -> str:
    return system.add_address_to_basket(body.customer_id, body.address)

#change amount of food in basket
@app.put("/basket/{food_id}/amount", tags=["Basket"])
async def change_amount(body: base.adjust_food_api) -> str:
    return system.change_amount(body.customer_id, body.food_id, body.amount)

#change size of food in basket
@app.put("/basket/{food_id}/size", tags=["Basket"])
async def change_size(body: base.adjust_food_api) -> str:
    return system.change_size(body.customer_id, body.food_id, body.size)

#review
@app.get("/restaurant", tags=['Review'])
async def get_restaurant_review(restaurant_id: str) -> list:
    return system.show_review(restaurant_id)

#add review to restaurant
@app.post("/restaurant", tags=["Review"])
async def add_restaurant_review(body: base.add_review_api) -> str:
    return system.add_review_to_restaurant(
        body.customer_id, body.rating, body.comment, 
        body.order_id, body.restaurant_id)

#remove review from restaurant
@app.delete("/restaurant", tags=["Review"])
async def remove_restaurant_review(customer_id: str ,restaurant_id: str) -> str:
    return system.remove_review_from_restaurant(customer_id, restaurant_id)

if __name__ == "__main__":
    uvicorn.run("ApiBackend:app", host="127.0.0.1", port=8000, log_level="info")