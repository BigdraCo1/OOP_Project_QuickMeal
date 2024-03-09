from internals.food import Food
from internals.review import Review


class Restaurant:
    def __init__(self, id: str, name_restaurant: str, restaurant_location: str, food_list, requested_order_list,
                 finished_order_list, reviewed_list: list[Review], owner):
        self.__restaurant_id = id
        self.__owner = owner
        self.__name_restaurant = name_restaurant
        self.__restaurant_location = restaurant_location
        self.__food_list = food_list
        self.__request_order_list = []
        self.__requested_order_list = requested_order_list
        self.__finished_order_list = finished_order_list
        self.__reviewed_list = reviewed_list
        if len(self.__reviewed_list) == 0:
            self.__rate = 0
        else:
            self.__rate = sum([review.rate for review in self.__reviewed_list]) / len(self.__reviewed_list)

    @property
    def rate(self):
        self.__rate = sum([review.rate for review in self.__reviewed_list])/len(self.__reviewed_list)
        return self.__rate


    @property
    def restaurant_id(self):
        return self.__restaurant_id

    @property
    def owner(self):
        return self.__owner

    @property
    def name_restaurant(self):
        return self.__name_restaurant

    @property
    def restaurant_location(self):
        return self.__restaurant_location

    @property
    def food_list(self):
        return self.__food_list

    @property
    def requested_order_list(self):
        return self.__requested_order_list

    @property
    def finished_order_list(self):
        return self.__finished_order_list

    @property
    def reviewed_list(self):
        return self.__reviewed_list
    
    @property
    def request_order_list(self):
        return self.__request_order_list
    
    @requested_order_list.setter
    def requested_order_list(self, order):
        self.__requested_order_list.append(order)

    @request_order_list.setter
    def request_order_list(self, order):
        self.__request_order_list.append(order)

    def search_menu(self, menu: str) -> object:
        for food in self.__food_list:
            food_name = food.name
            if menu == food_name:
                return food
        return 'This menu is not found'

    def remove_food(self, menu: str):
        food_list = self.food_list
        response = self.search_menu(menu)
        if isinstance(response, str):
            return response
        food_list.remove(response)
        del response
        return 'Removed Food from menu'

    def edit_menu(self, menu: str, request):
        food = self.search_menu(menu)
        if isinstance(food, Food):
            food.name = request.name
            food.type = request.type
            food.size = request.size
            food.price = request.price
            return vars(food)
        else:
            return 'This menu is not found'

    def add_menu(self, request):
        food_list = self.food_list
        new_menu = Food(request.name, request.type, request.size, request.price)
        food_list.append(new_menu)
        return new_menu

    def remove_request_order(self, order):
        self.__request_order_list.remove(order)

    def add_request_order(self, order):
        self.__request_order_list.append(order)

    def remove_requested_order(self, order):
        self.__requested_order_list.remove(order)

    def add_finished_order(self, order):
        self.__finished_order_list.append(order)

    def add_review(self, review):
        self.__reviewed_list.append(review)