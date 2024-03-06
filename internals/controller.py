from internals.rider_account import RiderAccount
from internals.restaurant_account import RestaurantAccount
from internals.custom_account import CustomerAccount
from internals.restaurant import Restaurant
from internals.review import Review

class Controller:
    def __init__(self, customer_account_list: list[CustomerAccount], rider_account_list: list[RiderAccount],
                 restaurant_list: list[RestaurantAccount]):
        self.__customer_account_list = customer_account_list
        self.__rider_account_list = rider_account_list
        self.__restaurant_account_list = restaurant_list
        self.__approval_list = None

    @property
    def customer_account_list(self):
        return self.__customer_account_list

    @property
    def rider_account_list(self):
        return self.__rider_account_list

    @property
    def restaurant_list(self):
        return self.__restaurant_account_list

    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant(self, new_restaurant: RestaurantAccount):
        self.__restaurant_account_list.append(new_restaurant)

    def remove_customer_account(self, customer: CustomerAccount):
        self.__customer_account_list.remove(customer)
        del customer

    def remove_rider_account(self, rider: RiderAccount):
        self.__rider_account_list.remove(rider)
        del rider

    def remove_restaurant(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, Restaurant):
            restaurant_acc = restaurant.owner
            restaurant_acc.remove_restaurant(restaurant)
            del restaurant
            return 'Success'
        return 'Not Found'

    def search_restaurant(self, name: str):
        for restaurant_account in self.__restaurant_account_list:
            response = restaurant_account.search_restaurant(name)
            if isinstance(response, Restaurant):
                return response
        return 'Not found restaurant'

    def get_menu_list(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, str):
            return restaurant
        return restaurant.food_list

    def search_menu_and_restaurant(self, key: str):
        show_list = []
        restaurant_list = self.restaurant_list
        for restaurant_acc in restaurant_list:
            for restaurant in restaurant_acc.restaurant_list:
                name = restaurant.name_restaurant
                restaurant_raw_attribute = vars(restaurant)
                restaurant_attributes = {key: value for key, value in restaurant_raw_attribute.items() if
                                         key != '_Restaurant__owner'}
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

    def edit_menu(self, restaurant, menu, request):
        acc_restaurant = self.search_restaurant(restaurant)
        if isinstance(acc_restaurant, str):
            return acc_restaurant
        return acc_restaurant.edit_menu(menu, request)

    def remove_menu(self, restaurant, menu):
        real_restaurant = self.search_restaurant(restaurant)
        if isinstance(real_restaurant, str):
            return real_restaurant
        return real_restaurant.remove_food(menu)

    def new_menu(self, restaurant, request):
        real_restaurant = self.search_restaurant(restaurant)
        return real_restaurant.add_menu(request)

    def search_current_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            if customer.current_order.order_id == search_order_id:
                return customer.current_order
        
    def search_customer_by_id(self, search_account_id):
        for customer in self.__customer_account_list:
            if customer.account_id == search_account_id:
                return customer
            
    def search_food_by_id(self, search_food_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return food
            
    def search_restaurant_by_id(self, search_restaurant_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                if restaurant.restaurant_id == search_restaurant_id:
                    return restaurant
                         
    def search_restaurant_by_food_id(self, search_food_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return food
                
    def search_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.order_list:
                if order.order_id == search_order_id:
                    return order
                
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
    
    def add_address_to_basket(self, customer_id, address):
        customer = self.search_customer_by_id(customer_id)
        order = customer.current_order
        order.customer_address = address
        return "the address of your order has been set!"
    
    def show_food_detail(self, food_id):
        food = self.search_food_by_id(food_id)
        return {"food_id"    : food.id,
                "food_name"  : food.name,
                "food_type"  : food.type,
                "food_size"  : food.size,
                "food_price" : food.price}
    
    def add_food_to_basket(self, customer_id, food_id, size, amount):
        customer = self.search_customer_by_id(customer_id)
        food = self.search_food_by_id(food_id)
        restaurant = self.search_restaurant_by_food_id(food_id)
        customer.add_food(food, size, amount)
        if restaurant not in customer.current_order.restaurant_list:
            customer.current_order.restaurant_list.append(restaurant)
        return str(amount) + str(food.food_name) + " is added to your cart!"

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
    
    def show_review(self, restaurant_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant.review_list == [] :
            return {}
        else:
            dct = {}
            for review in restaurant.review_list:
                dct[review.customer.profile.fullname] =  [review.rate, review.comment]
        return dct
    
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