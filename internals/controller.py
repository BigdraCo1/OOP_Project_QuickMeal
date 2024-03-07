from datetime import datetime

from internals.custom_account import CustomerAccount
from internals.rider_account import RiderAccount
from internals.restaurant_account import RestaurantAccount
from internals.restaurant import Restaurant
from internals.payment import Payment
from internals.review import Review

class Controller:
    def __init__(self, customer_account_list: list[CustomerAccount], 
                 rider_account_list: list[RiderAccount],
                 restaurant_account_list: list[RestaurantAccount]):
        self.__customer_account_list = customer_account_list
        self.__rider_account_list = rider_account_list
        self.__restaurant_account_list = restaurant_account_list
        self.__approval_list = None

    @property
    def customer_account_list(self):
        return self.__customer_account_list

    @property
    def rider_account_list(self):
        return self.__rider_account_list

    @property
    def restaurant_account_list(self):
        return self.__restaurant_account_list

    # [method] -> to add
    
    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant_account(self, new_restaurant: RestaurantAccount):
        self.__restaurant_account_list.append(new_restaurant)

    # [method] -> to remove
    
    def remove_customer_account(self, customer_account: CustomerAccount):
        self.__customer_account_list.remove(customer_account)
        del customer_account
        
    def remove_rider_account(self, rider_account: RiderAccount):
        self.__rider_account_list.remove(rider_account)
        del rider_account
        
    def remove_restaurant_account(self, restaurant_account: RestaurantAccount):
        self.__restaurant_account_list.remove(restaurant_account)
        del restaurant_account

    def remove_restaurant(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, Restaurant):
            restaurant_acc = restaurant.owner
            restaurant_acc.remove_restaurant(restaurant)
            del restaurant
            return 'Success'
        return 'Not Found'
    
    # [method] -> to search about customer_account
    
    def search_customer_by_id(self, search_account_id):
        for customer in self.customer_account_list:
            if customer.account_id == search_account_id:
                return customer
            
    def search_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.order_list:
                if order.order_id == search_order_id:
                    return order
            
    def search_current_order_by_id(self, search_order_id):
        for customer in self.customer_account_list:
            if customer.current_order.order_id == search_order_id:
                return customer.current_order
            
    # [method] -> to search about rider_account
    
    def search_rider_by_id(self, search_account_id):
        for rider in self.rider_account_list:
            if rider.account_id == search_account_id:
                return rider
    
    # [method] -> to search about restaurant_account
    
    def search_restaurant_by_id(self, search_restaurant_id):
        for restaurant_acc in self.restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                if restaurant.restaurant_id == search_restaurant_id:
                    return restaurant
    
    def search_restaurant(self, name: str):
        for restaurant_account in self.__restaurant_account_list:
            response = restaurant_account.search_restaurant(name)
            if isinstance(response, Restaurant):
                return response
        return 'Not found restaurant'
                         
    def search_restaurant_by_food_id(self, search_food_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return food
                    
    def search_food_by_id(self, search_food_id): # Is this method duplicated?
        for restaurant_acc in self.restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return food

    def search_menu_and_restaurant(self, key: str):
        show_list = []
        restaurant_list = self.restaurant_account_list
        for restaurant_acc in restaurant_list:
            for restaurant in restaurant_acc.restaurant_list:
                name = restaurant.name_restaurant
                restaurant_raw_attribute = vars(restaurant)
                restaurant_attributes = {key: value for key, value in restaurant_raw_attribute.items()
                                         if key != '_Restaurant__owner'}
                if key.lower() in name.lower():
                    show_list.append(restaurant_attributes)
                food_list = restaurant.food_list
                for food in food_list:
                    food_name = food.name
                    if key.lower() in food_name.lower() and restaurant_attributes not in show_list:
                        show_list.append(restaurant_attributes)
        if len(show_list) < 1:
            return 'Not Found'
        return show_list
    
    # [method] -> to show about customer_account
    
    def show_basket(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        order = customer.current_order
        order_dict = {}
        already_add = []
        if order != None :
            for food in order.food_list:
                if food not in already_add:
                    amount = len([f for f in order.food_list if f.name == food.name])
                    order_dict[amount] = [ food.id, food.name, food.price, food.current_size ]
                    already_add.append(food)
        return order_dict
    
    # [method] -> to show about rider_account
    
    
    
    # [method] -> to show about restaurant_account
    
    def show_restaurant(self):
        restaurant_dict = {}
        for restaurant_account in self.__restaurant_account_list:
            for restaurant in restaurant_account.restaurant_list:
                restaurant_dict[restaurant.restaurant_id] = [
                    restaurant.name_restaurant, restaurant.restaurant_location, restaurant.rate ]
        return restaurant_dict
    
    def show_restaurant_menu(self, restaurant_id):
        food_dict = {}
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for food in restaurant.food_list:
                food_dict[food.id] = [ food.name, food.price ]
        return food_dict
    
    def show_food_detail(self, food_id):
        food = self.search_food_by_id(food_id)
        return {"food_id"    : food.id,
                "food_name"  : food.name,
                "food_type"  : food.type,
                "food_size"  : food.size,
                "food_price" : food.price}
        
    def show_review(self, restaurant_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant.review_list == [] :
            return {}
        else:
            dct = {}
            for review in restaurant.review_list:
                dct[review.customer.profile.fullname] =  [review.rate, review.comment]
        return dct
    
    # [method] -> actions about customer_account
    
    def add_address_to_basket(self, customer_id, address):
        customer = self.search_customer_by_id(customer_id)
        order = customer.current_order
        order.customer_address = address
        return "the address of your order has been set!"
    
    def add_food_to_basket(self, customer_id, food_id, size, amount):
        customer = self.search_customer_by_id(customer_id)
        food = self.search_food_by_id(food_id)
        restaurant = self.search_restaurant_by_food_id(food_id)
        customer.add_food(food, size, amount)
        if restaurant not in customer.current_order.restaurant_list:
            customer.current_order.restaurant_list.append(restaurant)
        return str(amount) + str(food.food_name) + " is added to your cart!"
    
    def confirm_customer_order(self, customer_id, order_id):
        #search customer from customer_list 
        customer = self.search_customer_by_id(customer_id)
        if customer == None:
            return f"customer_id : {customer_id} not found"
        #search order from order_list
        order = customer.search_order_by_id(order_id)
        if order == None:
            return f"order_id : {order_id} not found"
        # calculate amount
        amount = sum(food.price for food in order.food_list)
        if customer.pocket.balance < amount:
            return "Insufficient balance"
        # pay out
        customer.pocket.pay_out(amount)
        # create payment object
        payment_time = datetime.now()
        food_list = []
        for food in order.food_list:
            food_list.append(food)
        # !!! about order_id change to order.order_id because idk how to random order_id from now
        payment = Payment(food_list,amount,"paid",order.restaurant_list,payment_time.strftime("%c"),order_id)
        order.order_state = "confirmed"
        order.payment = payment
        return [{"order_id": order.order_id, "order_state": order.order_state, "amount": amount}]
    
    def add_review_to_restaurant(self, customer_id, rating, comment, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        review = Review(rating, comment, customer, "TYPE")
        customer.reviewed_list.append(review)
        restaurant.reviewed_list.append(review)
        return "you have writing a review to " + str(restaurant.name_restaurant)
    
    def remove_review_from_restaurant(self, customer_id, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for review in restaurant.review_list:
            if review.customer == customer:
                restaurant.review_list.remove(review)
                customer.review_list.remove(review)
                del review
        return "you have remove a review from " + str(restaurant.name)
    
    # [method] -> actions about rider_account
    
    def receive_confirmed_customer_order(self, rider_id, customer_id, order_id):
        rider = self.search_rider_by_id(rider_id)
        if rider == None:
            return f"rider_id : {rider_id} not found"
        customer = self.search_customer_by_id(customer_id)
        if customer == None:
            return f"customer_id : {customer_id} not found"
        order = customer.search_order_by_id(order_id)
        if order == None:
            return f"order_id : {order_id} not found"
        if order.order_state == "confirmed":
            order.order_state = "received"
            order.rider = rider.account_id
            rider.add_received_order_food(order)
            for food in order.food_list:
                restaurant = self.search_restaurant_by_food_id(food.id)
                if restaurant not in order.restaurant_list:
                    order.restaurant_list.append(restaurant)
                restaurant.add_requested_order_food(food)
            return [{"order_id" : order.order_id, "order_state" : order.order_state, "rider_id" : order.rider}]
    
    # [method] -> actions about restaurant_account
    
    def get_menu_list(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, str):
            return restaurant
        return restaurant.food_list

    def new_menu(self, restaurant, request):
        real_restaurant = self.search_restaurant(restaurant)
        return real_restaurant.add_menu(request)

    def remove_menu(self, restaurant, menu):
        real_restaurant = self.search_restaurant(restaurant)
        if isinstance(real_restaurant, str):
            return real_restaurant
        return real_restaurant.remove_food(menu)
    
    def edit_menu(self, restaurant, menu, request):
        acc_restaurant = self.search_restaurant(restaurant)
        if isinstance(acc_restaurant, str):
            return acc_restaurant
        return acc_restaurant.edit_menu(menu, request)
    
    def process_cooking_order_food(self, restaurant_id, food_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant == None:
            return f"restaurant_id : {restaurant_id} not found"
        
    
    # [method] about order 

    def change_amount(self, customer_id, food_id, amount, new_amount, size):
        customer = self.search_customer_by_id(customer_id)
        food = self.search_food_by_id(food_id)
        restaurant = self.search_restaurant_by_food_id(food_id)
        customer.remove_food(food_id, size, amount)
        customer.add_food(food, size, new_amount)
        if restaurant not in customer.current_order.restaurant_list:
            customer.current_order.restaurant_list.append(restaurant)
        return str(food.food_name) + " is now" + str(new_amount)

    def change_size(self, customer_id, food_id, size, new_size):
        customer = self.search_customer_by_id(customer_id)
        order = customer.current_order
        food = self.search_food_by_id(food_id)
        for customer_food in order.food_list:
            if customer_food.id == food.id and customer_food.current_size == size:
                customer_food.current_size = new_size
        return str(food.food_name) + " is now" + str(new_size)