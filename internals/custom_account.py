from internals.account import Account, Profile
from internals.food import Food
from internals.order import Order
from internals.pocket import Pocket

class CustomerAccount(Account):
    def __init__(self, account_id: str, password: str, profile: Profile, pocket : Pocket):
        if not isinstance(profile, Profile, Pocket):
            ValueError("Error")
        super().__init__(account_id, password, profile, Pocket)
        self.__address_list = []
        self.__reviewed_list = []
        self.__current_order = None
        self.__order_list = []

    @property
    def current_order(self):
        return self.__current_order

    @current_order.setter
    def current_order(self, order):
        self.__current_order = order
    
    @property
    def order_list(self):
        return self.__order_list

    @property
    def reviewed_list(self):
        return self.__reviewed_list

    def add_address(self, address: str):
        self.__address_list.append(address)

    def remove_address(self, address: str):
        self.__address_list.remove(address)

    def add_food(self, food, size, amount):
        if self.__current_order == None :
            self.create_basket()
        customer_food = Food(food.id, food.name, food.type, food.size, food.price, size)
        for i in range (amount):
            self.__current_order.food_list.append(customer_food)
    
    def create_basket(self):
        self.__current_order = Order(self)
        self.__current_order.state = 'Not Comfirm'

    def remove_food(self, food_id, size, amount):
        for i in range(amount):
            for food in self.__current_order.food_list:
                if food.id == food_id and food.current_size == size:
                    self.__current_order.food_list.remove(food)
        
    # use for search order by order_id in 
    # current_order:list (cart) to confirm order
    def search_order_by_id(self, order_id):
        for order in self.__current_order:
            if order.order_id == order_id: return order
        return None
    
    def add_current_order(self, order):
        self.__current_order.append(order)

    def add_order_list(self, order):
        self.__order_list.append(order)