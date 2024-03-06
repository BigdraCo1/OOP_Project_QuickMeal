from constants.restaurant import *
from constants.account import *
from constants.profiles import *
from constants.food import *
from constants.order import *
from internals.controller import Controller

system = Controller([],
                    [],
                    [])

system.add_restaurant(restaurant_owner_account1)
system.add_restaurant(restaurant_owner_account2)
restaurant_owner_account1.assign_restaurant(restaurant1)
restaurant_owner_account1.assign_restaurant(restaurant2)
restaurant_owner_account2.assign_restaurant(restaurant3)

system.add_restaurant(restaurant_owner_account3)
system.add_customer_account(customer_account1)
system.add_rider_account(rider_account1)
restaurant_owner_account3.assign_restaurant(restaurant4)
customer_account1.current_order = []
customer_account1.add_current_order(order1)
customer_account1.add_current_order(order2)
rider_account1.recieve_order_list = order1
rider_account1.recieve_order_list = order2
restaurant4.requested_order_list = order1
restaurant4.requested_order_list = order2