from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

from constants import account, restaurant
from internals import controller

system = controller.Controller([],
                               [],
                               [])

system.add_restaurant(account.restaurant_owner_account1)
system.add_restaurant(account.restaurant_owner_account2)
account.restaurant_owner_account1.assign_restaurant(restaurant.restaurant1)
account.restaurant_owner_account1.assign_restaurant(restaurant.restaurant2)
account.restaurant_owner_account2.assign_restaurant(restaurant.restaurant3)
class ClassController:
    def __init__(self):
        self.__customer_account_list = []
        self.__restaurant_account_list = []
        self.__cc_food_list = []
    
    @property
    def customer_account_list(self):
        return self.__customer_account_list
    
    @customer_account_list.setter
    def customer_account_list(self, new):
        self.__customer_account_list = new

    @property
    def restaurant_account_list(self):
        return self.__restaurant_account_list
    
    @restaurant_account_list.setter
    def restaurant_account_list(self, new):
        self.__restaurant_account_list = new

    @property
    def cc_food_list(self):
        return self.__cc_food_list
    
    @cc_food_list.setter
    def cc_food_list(self, new):
        self.__cc_food_list = new

    def search_current_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            if customer.current_order.order_id == search_order_id:
                return customer.current_order
        
    def search_customer_by_id(self, search_account_id):
        for customer in self.__customer_account_list:
            if customer.account_id == search_account_id:
                return customer
            
    def search_food_by_id(self, search_food_id):
        for restaurant in self.__restaurant_account_list:
            for food in restaurant.restaurant_food_list :
                if food.food_id == search_food_id:
                    return food
            
    def search_restaurant_by_id(self, search_restaurant_id):
        for restaurant in self.__restaurant_account_list:
            if restaurant.account_id == search_restaurant_id:
                return restaurant   
                         
    def search_restaurant_by_food_id(self, search_food_id):
        for restaurant in self.__restaurant_account_list:
            for food in restaurant.restaurant_food_list:
                if food.food_id == search_food_id:
                    return food
                
    def search_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.order_list:
                if order.order_id == search_order_id:
                    return order
            
    def show_cart(self, account_id):
        customer = self.search_customer_by_id(account_id)
        order = customer.current_order
        if order == None :
            return []
        else:
            return [food.food_name for food in order.order_food_list]
            
    def add_food_to_cart(self, account_id, food_id):
        customer = self.search_customer_by_id(account_id)
        food = self.search_food_by_id(food_id)
        customer.add_food(food)
        return str(food.food_name) + " is added to your cart!"
    
    def remove_food_from_cart(self, account_id, food_id):
        customer = self.search_customer_by_id(account_id)
        food = self.search_food_by_id(food_id)
        customer.remove_food(food)
        return str(food.food_name) + " is remove from your cart!"
    
    def show_review(self, restaurant_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant.review_list == [] :
            return []
        else:
            lst = []
            for review in restaurant.review_list:
                lst.append([review.owner.name, review.rate, review.comment])
        return lst
    
    def add_review_to_restaurant(self, customer_id, rating, comment, order_id, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        order = self.search_order_by_id(order_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        review = Review(customer, rating, comment, order)
        customer.review_list.append(review)
        for restaurant in order.restaurant_list:
            if restaurant.account_id == restaurant_id:
                restaurant.review_list.append(review)
        return "you have writing a review to " + str(restaurant.name)
    
    def remove_review_from_restaurant(self, customer_id, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for review in restaurant.review_list:
            if review.owner == customer:
                restaurant.review_list.remove(review)
                customer.review_list.remove(review)
                del review
        return "you have remove a review from " + str(restaurant.name)

class Account :
    def __init__(self, account_id):
        self.__account_id = account_id

    @property
    def account_id(self):
        return self.__account_id

class Customer(Account) :
    def __init__(self, account_id, name):
        super().__init__(account_id)
        self.__name = name
        self.__current_order = None
        self.__review_list = []
        self.__order_list = []

    @property
    def name(self):
        return self.__name

    @property
    def current_order(self):
        return self.__current_order
    
    @property
    def review_list(self):
        return self.__review_list
    
    @review_list.setter
    def review_list(self, new):
        self.__review_list = new
    
    @property
    def order_list(self):
        return self.__order_list
    
    @order_list.setter
    def order_list(self, new):
        self.__order_list = new
    
    def get_customer_detail(self):
        return {
            "account_id": self.account_id,
            "current_order": self.__current_order
        }

    def add_food(self, food):
        if self.__current_order == None :
            self.create_order()
        self.__current_order.order_food_list.append(food)

    def remove_food(self, food):
        self.__current_order.order_food_list.remove(food)
    
    def create_order(self):
        self.__current_order = Order(self)
        self.__current_order.state = 'Not Comfirm'
        return "Done"
    
class Restaurant(Account) :
    def __init__(self, account_id, name):
        super().__init__(account_id)
        self.__name = name
        self.__restaurant_food_list = []
        self.__review_list = []
        
    @property
    def name(self):
        return self.__name

    def add_food(self, food):
        self.__restaurant_food_list.append(food)

    def add_review(self, review):
        self.__review_list.append(review)

    @property
    def restaurant_food_list(self):
        return self.__restaurant_food_list
    
    @property
    def review_list(self):
        return self.__review_list

class Order :
    ID = 1
    def __init__(self, customer, restaurant_list = [], order_food_list = []):
        self.__order_id = str(Order.ID)
        self.__customer = customer
        self.__restaurant_list = restaurant_list
        self.__order_food_list = order_food_list
        self.__state = None
        Order.ID += 1

    @property
    def customer(self):
        return self.__customer

    @property
    def order_id(self):
        return self.__order_id
    
    @property
    def restaurant_list(self):
        return self.__restaurant_list
    
    @property
    def order_food_list(self):
        return self.__order_food_list
    
    @order_food_list.setter
    def order_food_list(self, new):
        self.__order_food_list = new
    
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, new):
        self.__state = new

class Food :
    def __init__(self, food_id, food_name, food_price):
        self.__food_id = food_id
        self.__food_name = food_name
        self.__food_price = food_price

    @property
    def food_name(self):
        return self.__food_name
    
    @property
    def food_id(self):
        return self.__food_id
    
class Review :
    def __init__(self, owner, rate, comment, order):
        self.__owner = owner
        self.__rate = rate
        self.__comment = comment

    @property
    def owner(self):
        return self.__owner
    
    @property
    def rate(self):
        return self.__rate
    
    @property
    def comment(self):
        return self.__comment

class add_food_api(BaseModel):
    account_id: str
    food_id: str

class add_review_api(BaseModel):
    customer_id: str 
    rating: int 
    comment: str
    order_id: str 
    restaurant_id: str

class remove_review_api(BaseModel):
    customer_id: str 
    restaurant_id: str

controller = ClassController()  
customer1 = Customer('101', 'Ken')
restaurant1 = Restaurant('201', 'ร้านอาหาร 1')
food1 = Food('001', 'ข้าวมันไก่', 60)
food2 = Food('002', 'ไก่ทอด', 40)

controller.customer_account_list.append(customer1)
controller.restaurant_account_list.append(restaurant1)
controller.cc_food_list.append(food1)
controller.cc_food_list.append(food2)
restaurant1.add_food(food1)
restaurant1.add_food(food2)

#Cart
# GET -- > Read Current Order
@app.get("/cart", tags=['Cart'])
async def get_order(account_id: str) -> list:
    return controller.show_cart(account_id)

# Post -- > Add Food To Current Order
@app.post("/cart", tags=["Cart"])
async def add_food(body: add_food_api) -> str:
    return controller.add_food_to_cart(body.account_id, body.food_id)

# DELETE --> Remove Food From Current Order
@app.delete("/cart", tags=["Cart"])
async def remove_food(body: add_food_api) -> str:
    return controller.remove_food_from_cart(body.account_id, body.food_id)

order1 = Order(customer1, [restaurant1], [food1, food2])
customer1.order_list.append(order1)

#Review
# GET -- > Read Review of Restaurant
@app.get("/restaurant", tags=['Review'])
async def get_restaurant_review(restaurant_id: str) -> list:
    return controller.show_review(restaurant_id)

# Post -- > Add Review To Restaurant
@app.post("/restaurant", tags=["Review"])
async def add_restaurant_review(body: add_review_api) -> str:
    return controller.add_review_to_restaurant(
        body.customer_id, body.rating, body.comment, 
        body.order_id, body.restaurant_id)

# DELETE --> Remove Review From Restaurant
@app.delete("/restaurant", tags=["Review"])
async def remove_restaurant_review(body: remove_review_api) -> str:
    return controller.remove_review_from_restaurant(body.customer_id, body.restaurant_id)

order1 = Order(customer1, [restaurant1], [food1, food2])
customer1.order_list.append(order1)

if __name__ == "__main__":
    uvicorn.run("API_cool:app", host="127.0.0.1", port=8000, log_level="info")