from internals.account import Account, Profile
from internals.order import Order


class RiderAccount(Account) :
    def __init__(self,account_id : str, password : str, profile = None):
        super().__init__(account_id, password, profile)
        self.__received_order_list = []
        self.__holding_order_list = []
        self.__review_list = []
        # getter

    #there is change in correcting word
    @property
    def received_order_list(self):
        return self.__received_order_list

    # setter
    @received_order_list.setter
    def received_order_list(self, order):
        self.__received_order_list.append(order)

    @property #why it have the same setter as the above property?
    def order_list(self):
        return self.__received_order_list

    #increase method
    def add_received_order(self, order: Order):
        self.__received_order_list.append(order)

    def remove_received_order(self, order: Order):
        self.__received_order_list.remove(order)
        
    def add_holding_order(self, order: Order):
        self.__holding_order_list.append(order)
        
    def remove_holding_order(self, order: Order):
        self.__holding_order_list.remove(order)
        
    def search_order_by_id(self, order_id):
        for order in self.__received_order_list:
            if order.order_id == order_id:
                return order
            
    def search_holding_order_by_id(self, order_id):
        for order in self.__holding_order_list:
            if order.order_id == order_id:
                return order
        return None