from internals.restaurant_account import RestaurantAccount


class Payment:
    def __init__(self, amount: float, payment_method: str, paid_to: RestaurantAccount, date_time: str, transaction_id: str):
        self.__food_list = []
        self.__amount = amount
        self.__payment_method = payment_method
        self.__paid_to = paid_to
        self.__date_time = date_time
        self.__transaction_id = transaction_id