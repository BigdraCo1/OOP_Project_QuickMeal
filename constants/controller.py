from constants.restaurant import *
from constants.account import *
from constants.profiles import *
from constants.food import *
from constants.order import *
from internals.controller import Controller

system = Controller([],
                    [],
                    [])

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

for review in review_list1:
    restaurant1.add_reviewed(review)

for review in review_list2:
    restaurant2.add_reviewed(review)

for review in review_list3:
    restaurant3.add_reviewed(review)

for review in review_list4:
    restaurant4.add_reviewed(review)

customer_account1.add_order_list(order1)
customer_account1.add_order_list(order2)
rider_account1.recieve_order_list = order1
rider_account1.recieve_order_list = order2
restaurant4.add_requested(order1)
#restaurant4.add_requested(order2)