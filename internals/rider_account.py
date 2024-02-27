from account import Account, Profile
from order import Order
class RiderAccount(Account):
    def __init__(self, account_id: str, password: str, profile: Profile, recieve_order_list, reviewed_list):
        super().__init__(account_id, password, profile)
        self.__recieve_order_list = recieve_order_list
        self.__reviewed_list = reviewed_list

    def add_order(self, order: Order):
        self.__recieve_order_list.append(order)

    def remove_order(self, order: Order):
        self.__recieve_order_list.remove(order)