from internals.account import Account, Profile
from internals.order import Order


class RiderAccount(Account) :
    def __init__(self,account_id : str, password : str, profile = None):
        super().__init__(account_id, password, profile)
        self.__recieve_order_list = []
        self.__review_list = []
        # getter

    @property
    def recieve_order_list(self):
        return self.__recieve_order_list

    # setter
    @recieve_order_list.setter
    def recieve_order_list(self, order):
        self.__recieve_order_list.append(order)

    @property
    def order_list(self):
        return self.__recieve_order_list

    def add_order(self, order: Order):
        self.__recieve_order_list.append(order)

    def remove_order(self, order: Order):
        self.__recieve_order_list.remove(order)