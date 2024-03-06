from constants import account, restaurant, food, profiles, order
from internals.controller import Controller

system = Controller([],
                    [],
                    [])

system.add_restaurant_account(account.restaurant_owner_account1)
system.add_restaurant_account(account.restaurant_owner_account2)
system.add_restaurant_account(account.restaurant_owner_account3)
system.add_customer_account(account.customer_account1)
system.add_rider_account(account.rider_account1)
account.restaurant_owner_account1.assign_restaurant(restaurant.restaurant1)
account.restaurant_owner_account1.assign_restaurant(restaurant.restaurant2)
account.restaurant_owner_account2.assign_restaurant(restaurant.restaurant3)
account.restaurant_owner_account3.assign_restaurant(restaurant.restaurant4)
account.customer_account1.current_order = order.order1
account.customer_account1.current_order = order.order2
account.rider_account1.current_order = order.order1
account.rider_account1.current_order = order.order2
restaurant.restaurant4.current_order_list = order.order1
restaurant.restaurant4.current_order_list = order.order2
