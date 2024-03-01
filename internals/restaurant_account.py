from account import Account, Profile
from restaurant import Restaurant
class RestaurantAccount(Account):
    def __init__(self, account_id: str, password: str, profile: Profile):
        super().__init__(account_id, password, profile)
        self.__restaurant_list = []

    def search_restaurant(self, name):
        for restaurant in self.restaurant_list:
            if restaurant.name_restaurant == name:
                return restaurant
        return 'Not Found restaurant'

    @property
    def restaurant_list(self):
        return self.__restaurant_list

    def assign_restaurant(self, restaurant: Restaurant):
        self.__restaurant_list.append(restaurant)