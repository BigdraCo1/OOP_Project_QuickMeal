from internals.restaurant_account import RestaurantAccount

class Payment:
    def __init__(self, amount: float, payment_method: str, paid_to: RestaurantAccount, date_time: str, transaction_id: str, payment_status: str):
        self.__food_list = []
        self.__amount = amount
        self.__payment_method = payment_method
        self.__paid_to = paid_to
        self.__date_time = date_time
        self.__transaction_id = transaction_id
        self.__payment_status = payment_status

    #getter
    @property
    def amount(self):
        return self.__amount
    @property
    def payment_status(self):
        return self.__payment_status
    @property
    def transaction_id_id(self):
        return self.__transaction_id_id
    #setter
    @payment_status.setter
    def payment_status(self, status: str):
        self.__payment_status = status
    