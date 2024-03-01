from rider_account import RiderAccount
from restaurant_account import RestaurantAccount, Restaurant
from custom_account import CustomerAccount


class Controller:
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

    def remove_restaurant(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, Restaurant):
            restaurant_acc = restaurant.owner
            restaurant_acc.remove_restaurant(restaurant)
            del restaurant
            return 'Success'
        return 'Not Found'

    def search_restaurant(self, name: str):
        for restaurant_account in self.__restaurant_list:
            response = restaurant_account.search_restaurant(name)
            if isinstance(response, Restaurant):
                return response
        return 'Not found restaurant'

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
