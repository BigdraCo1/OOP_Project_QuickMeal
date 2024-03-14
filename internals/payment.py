from uuid import uuid4


class Payment:
    def __init__(self, amount: float, payment_method: str, paid_to: object, date_time: str, payment_status: str, order_id = None):
        self.__food_list = []
        self.__order_id = order_id
        self.__amount = amount
        self.__payment_method = payment_method
        self.__paid_to = paid_to
        self.__date_time = date_time
        self.__transaction_id = uuid4()
        self.__payment_status = payment_status

    #getter

    @property
    def order_id(self):
        return self.__order_id

    @property
    def amount(self):
        return self.__amount

    @property
    def payment_status(self):
        return self.__payment_status

    @property
    def transaction_id(self):
        return self.__transaction_id

    #setter
    @payment_status.setter
    def payment_status(self, status: str):
        self.__payment_status = status
    