from constants import account, restaurant
from internals import controller

system = controller.Controller([],
                               [],
                               [])

system.add_restaurant(account.restaurant_owner_account1)
system.add_restaurant(account.restaurant_owner_account2)
account.restaurant_owner_account1.assign_restaurant(restaurant.restaurant1)
account.restaurant_owner_account1.assign_restaurant(restaurant.restaurant2)
account.restaurant_owner_account2.assign_restaurant(restaurant.restaurant3)