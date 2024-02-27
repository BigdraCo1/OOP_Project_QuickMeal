from account import Account, Profile
from food import Food
from order import Order
from review import Review
class RestaurantAccount(Account):
    def __init__(self, name_restaurant: str,account_id: str, password: str, profile: Profile, restaurant_location: str, food_list,
                 requested_order_list, finished_order_list, reviewed_list):
        super().__init__(account_id, password, profile)
        self.__restaurant = name_restaurant
        self.__restaurant_location = restaurant_location
        self.__food_list = food_list
        self.__requested_order_list = requested_order_list
        self.__finished_order_list = finished_order_list
        self.__reviewed_list = reviewed_list

    @property
    def name_restaurant(self):
        return self.__restaurant

    @property
    def food_list(self):
        return self.__food_list

    def add_location(self, location: str):
        self.__restaurant_location = location

    def remove_location(self, location: str):
        self.__restaurant_location = location

    def add_food(self, food: Food):
        self.__food_list.append(food)

    def remove_food(self, food: Food):
        self.__food_list.remove(food)

    def add_requested_order(self, order: Order):
        self.__requested_order_list.append(order)

    def remove_requested_order(self, order: Order):
        self.__requested_order_list.remove(order)

    def add_finished_order(self, order: Order):
        self.__finished_order_list.append(order)

    def remove_finished_order(self, order: Order):
        self.__finished_order_list.remove(order)

    def add_reviewed(self, review: Review):
        self.__reviewed_list.append(review)

    def remove_reviewed(self, review: Review):
        self.__reviewed_list.remove(review)