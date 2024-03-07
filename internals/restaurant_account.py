from internals.account import Account, Profile


class RestaurantAccount(Account):
    def __init__(self, account_id: str, password: str, profile: Profile, pocket : object):
        super().__init__(account_id, password, profile, pocket)
        self.__restaurant_list = []

    def search_restaurant(self, name):
        for restaurant in self.restaurant_list:
            if restaurant.name_restaurant == name:
                return restaurant
        return 'Not Found restaurant'

    @property
    def restaurant_list(self):
        return self.__restaurant_list

    def assign_restaurant(self, restaurant):
        self.__restaurant_list.append(restaurant)

    def remove_restaurant(self, restaurant):
        self.__restaurant_list.remove(restaurant)