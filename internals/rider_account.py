from internals.account import Account, Profile
from internals.order import Order


class RiderAccount(Account) :
    def __init__(self,account_id : str, password : str, profile = None, pocket = None):
        super().__init__(account_id, password, profile, pocket)
        self.__request_order_list = [] # all riders have all confirmed orders
        self.__receive_order_list = []
        self.__finished_order_list = []
        self.__review_list = []
        # getter

    @property
    def request_order_list(self):
        return self.__request_order_list
        
    @property
    def recieve_order_list(self):
        return self.__receive_order_list
        
    @property
    def finished_order_list(self):
        return self.__finished_order_list

    @property  # what the hell is variable?
    def order_list(self):
        return self.__request_order_list

    def add_order(self, order: Order):
        self.__request_order_list.append(order)

    def remove_order(self, order: Order):
        self.__request_order_list.remove(order)
        
    # right word and format methods
        
    def add_request_order(self, order: Order):
        self.__request_order_list.append(order)

    def remove_request_order(self, order: Order):
        self.__request_order_list.remove(order)
        
    def add_receive_order(self, order: Order):
        self.__receive_order_list.append(order)

    def remove_receive_order(self, order: Order):
        self.__receive_order_list.remove(order)
        
    def add_finished_order(self, order: Order):
        self.__finished_order_list.append(order)

    def remove_finished_order(self, order: Order):
        self.__finished_order_list.remove(order)
        
    def search_request_order_by_id(self, order_id):
        for order in self.__request_order_list:
            if order.order_id == order_id: return order
        return None
    
    def search_receive_order_by_id(self, order_id):
        for order in self.__receive_order_list:
            if order.order_id == order_id: return order
        return None
    
    def search_finished_order_by_id(self, order_id):
        for order in self.__finished_order_list:
            if order.order_id == order_id: return order
        return None