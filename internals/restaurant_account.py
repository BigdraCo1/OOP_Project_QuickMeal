from internals.account import Account, Profile


class RestaurantAccount(Account):
    ID = 1

    def __init__(self, password: str, profile: Profile, pocket: object):
        super().__init__(f"RA{RestaurantAccount.ID}", password, profile, pocket)
        RestaurantAccount.ID += 1
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
