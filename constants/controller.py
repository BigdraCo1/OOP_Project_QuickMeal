from constants.restaurant import *
from constants.account import *
from constants.profiles import *
from constants.food import *
from constants.order import *
from internals.controller import Controller
from internals.pocket import Pocket

system = Controller([],
                    [],
                    [],
                    Pocket(1000000))

system.add_restaurant_account(restaurant_owner_account1)
system.add_restaurant_account(restaurant_owner_account2)
restaurant_owner_account1.assign_restaurant(restaurant1)
restaurant_owner_account1.assign_restaurant(restaurant2)
restaurant_owner_account2.assign_restaurant(restaurant3)

system.add_restaurant_account(restaurant_owner_account3)
system.add_customer_account(customer_account1)
system.add_customer_account(customer_account2)
system.add_rider_account(rider_account1)
restaurant_owner_account3.assign_restaurant(restaurant4)