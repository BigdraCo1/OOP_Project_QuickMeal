from constants.restaurant import *
from constants.account import *
from internals.controller import Controller

system = Controller([],
                    [],
                    [])

system.add_restaurant_account(restaurant_owner_account1)
system.add_restaurant_account(restaurant_owner_account2)
restaurant_owner_account1.assign_restaurant(restaurant1)
restaurant_owner_account1.assign_restaurant(restaurant2)
restaurant_owner_account2.assign_restaurant(restaurant3)