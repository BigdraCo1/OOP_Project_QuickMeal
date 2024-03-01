from internals.payment import Payment
class Order:
    def __init__(self, order_id, customer, rider, customer_address, order_status, payment: Payment):
        self.__order_id = order_id
        self.__customer = customer
        self.__customer_address = customer_address
        self.__restaurant_list = []
        self.__food_list = []
        self.__rider = rider
        self.__order_status = order_status
        self.__payment = payment
