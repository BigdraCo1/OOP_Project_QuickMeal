from databases import database
import base

from fastapi import FastAPI
import uvicorn

app = FastAPI()
#Show
@app.get("/show/restaurant", tags=["Show"])
async def show_restaurant() -> dict:
    return system.show_restaurant()

@app.get("/menu/{restaurant_id}", tags=["Show"])
async def restaurant_menu(restaurant_id: str) -> dict:
    return system.show_restaurant_menu(restaurant_id)

@app.get("/show/{food_id}", tags=["Show"])
async def food_detail(food_id: str) -> dict:
    return system.show_food_detail(food_id)

#Basket
@app.post("/show/{food_id}", tags=["Basket"])
async def add_food(body: base.add_food_api) -> str:
    return system.add_food_to_basket(body.customer_id, body.food_id, body.size, body.amount)

@app.get("/basket", tags=["Basket"])
async def get_basket(customer_id: str) -> dict:
    return system.show_basket(customer_id)

@app.post("/basket/address", tags=["Basket"])
async def add_address(body: base.add_address_api) -> str:
    return system.add_address_to_basket(body.customer_id, body.address)

@app.put("/basket/{food_id}/amount", tags=["Basket"])
async def change_amount(body: base.change_amount_api) -> str:
    return system.change_amount(body.customer_id, body.food_id, body.amount)

@app.put("/basket/{food_id}/size", tags=["Basket"])
async def change_size(body: base.change_size_api) -> str:
    return system.change_size(body.customer_id, body.food_id, body.size)

#Review
@app.get("/restaurant", tags=['Review'])
async def get_restaurant_review(restaurant_id: str) -> list:
    return system.show_review(restaurant_id)

@app.post("/restaurant", tags=["Review"])
async def add_restaurant_review(body: base.add_review_api) -> str:
    return system.add_review_to_restaurant(
        body.customer_id, body.rating, body.comment, 
        body.order_id, body.restaurant_id)

@app.delete("/restaurant", tags=["Review"])
async def remove_restaurant_review(customer_id: str ,restaurant_id: str) -> str:
    return system.remove_review_from_restaurant(customer_id, restaurant_id)

if __name__ == "__main__":
    uvicorn.run("ApiBackend:app", host="127.0.0.1", port=8000, log_level="info")