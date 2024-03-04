from internals import order
from internals import payment
from constants import account
from constants import restaurant
from constants import food

order1 = order.Order(
    order_id = "Order_ID",
    customer = account.customer_account1,
    rider = account.rider_account1,
    restaurant_list = [restaurant.restaurant4],
    food_list = [food.fried_chicken],
    order_state = "Get_Restaurant",
    payment = payment.Payment(food.fried_chicken.price,"Online",restaurant.restaurant4,"2021-01-01 12:00:00","P1","Paid"))
order2 = order.Order(
    order_id = "Order_ID2",
    customer = account.customer_account1,
    rider = account.rider_account1,
    restaurant_list = [restaurant.restaurant4],
    food_list = [food.fried_chicken,food.grilled_chicken],
    order_state = "Get_Restaurant",
    payment = payment.Payment(food.fried_chicken.price + food.grilled_chicken.price,"Online",restaurant.restaurant4,"2021-01-01 12:00:00","P2","Paid"))
