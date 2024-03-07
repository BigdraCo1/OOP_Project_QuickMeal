from internals.account import Account, Profile
from internals.order import Order


class RiderAccount(Account) :
    def __init__(self,account_id : str, password : str, profile = None):
        super().__init__(account_id, password, profile)
        self.__received_order_food_list = []
        self.__holding_order_food_list = []
        self.__review_list = []
        # getter

    #there is change in correcting word
    @property
    def received_order_list(self):
        return self.__received_order_food_list

    # setter
    @received_order_list.setter
    def received_order_list(self, order_food):
        self.__received_order_food_list.append(order_food) # what append in setter?
        # self.__received_order_food_list = order_food
        
    @property
    def holding_order_list(self):
        return self.__holding_order_food_list
    
    @holding_order_list.setter
    def holding_order_list(self, order_food):
        self.__holding_order_food_list = order_food

    # @property #why it have the same setter as the above property?
    # def order_list(self):
    #     return self.__received_food_order_list

    #increase method
    def add_received_order_food(self, order: Order):
        self.__received_order_food_list.append(order)
        
    def add_holding_order_food(self, order: Order):
        self.__holding_order_food_list.append(order)

    def remove_received_order_food(self, order: Order):
        self.__received_order_food_list.remove(order)
        
    def remove_holding_order_food(self, order: Order):
        self.__holding_order_food_list.remove(order)
        
    def search_received_order_food_by_id(self, order_id):
        for order in self.__received_order_food_list:
            if order.order_id == order_id:
                return order
        return None
            
    def search_holding_order_food_by_id(self, order_id):
        for order in self.__holding_order_food_list:
            if order.order_id == order_id:
                return order
        return None