from internals.order import *
from internals.payment import *
from constants.account import *
from constants.restaurant import *
from constants.food import *

order1 = Order(
    customer = customer_account1,
    customer_address=None,
    rider = rider_account1,
    restaurant = restaurant4,
    food_list = [fried_chicken],
    order_state = "Get_Restaurant",
    payment = Payment(fried_chicken.price,"Online",restaurant4,"2021-01-01 12:00:00","Paid")
)
order2 = Order(
    customer = customer_account1,
    customer_address=None,
    rider = rider_account1,
    restaurant = restaurant4,
    food_list = [fried_chicken, grilled_chicken],
    order_state = "Get_Restaurant",
    payment = Payment(fried_chicken.price + grilled_chicken.price,"Online",restaurant4,"2021-01-01 12:00:00","Paid")
)
order3 = Order(
    customer = customer_account1,
    customer_address=None,
    rider = None,
    restaurant = restaurant4,
    food_list = [fried_chicken, grilled_chicken],
    order_state = "Unconfirmed",
    payment = None
)
order4 = Order(
    customer = customer_account1,
    customer_address=None,
    rider = None,
    restaurant = restaurant4,
    food_list = [fried_chicken],
    order_state = "Unconfirmed",
    payment = None
)