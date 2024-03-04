import internals.food as Food

class Restaurant :
    def __init__(self,restaurant_id: str, restaurant_name: str, restaurant_location: str, food_list: list = [] ,requested_order_list: list = None,
                 current_order_list: list = [], finished_order_list: list = [], reviewed_list = [], owner = None):
        self.__restaurant_id = id
        self.__owner = owner
        self.__restaurant_name = restaurant_name
        self.__restaurant_location = restaurant_location
        self.__food_list = food_list
        self.__request_order_list = requested_order_list
        self.__current_order_list = current_order_list
        self.__finished_order_list =  finished_order_list
        self.__review_list = reviewed_list
        
    #getter
    @property
    def current_order_list(self):
        return self.__current_order_list
    @property
    def restaurant_name(self):
        return self.__restaurant_name
    @property
    def food_list(self):
        return self.__food_list
    #setter
    @current_order_list.setter
    def current_order_list(self, order):
        self.__current_order_list.append(order)
    @food_list.setter
    def food_list(self, food : Food):
        self.__food_list.append(food)

    #method
    def remove_current_order(self, order):
        self.__current_order_list.remove(order)
    def get_order_list(self):
        return self.__current_order_list
    def search_food_by_name(self, food_name : str):
        for food in self.__food_list:
            if food.name == food_name:
                return food