from rider_account import RiderAccount
from restaurant_account import RestaurantAccount
from custom_account import CustomerAccount
class Controller():
    def __init__(self, customer_account_list: list[CustomerAccount], rider_account_list: list[RiderAccount],
                 restaurant_list: list[RestaurantAccount]):
        self.__customer_account_list = customer_account_list
        self.__rider_account_list = rider_account_list
        self.__restaurant_list = restaurant_list
        self.__approval_list = None

    @property
    def customer_account_list(self):
        return self.__customer_account_list

    @property
    def rider_account_list(self):
        return self.__rider_account_list

    @property
    def restaurant_list(self):
        return self.__restaurant_list

    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant(self, new_restaurant: RestaurantAccount):
        self.__restaurant_list.append(new_restaurant)

    def remove_customer_account(self, customer: CustomerAccount):
        self.__customer_account_list.remove(customer)
        del customer

    def remove_rider_account(self, rider: RiderAccount):
        self.__rider_account_list.remove(rider)
        del rider

    def remove_restaurant(self, restaurant: RestaurantAccount):
        self.__restaurant_account_list.remove(restaurant)
        del restaurant

    def search_restaurant(self, name: str):
        for restaurant in self.__restaurant_list:
            if restaurant.get_name() == name: return restaurant

    def search_menu_and_restaurant(self, key: str):
        show_list = []
        restaurant_list = self.restaurant_list
        for restaurant in restaurant_list:
            name = restaurant.name_restaurant
            if key.lower() in name.lower():
                show_list.append(vars(restaurant))
            food_list = restaurant.food_list
            for food in food_list:
                food_name = food.name
                if key.lower() in food_name.lower() and vars(restaurant) not in show_list:
                    show_list.append(vars(restaurant))
        return show_list