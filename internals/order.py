class Order:
    def __init__(self,order_id = None, customer = None,customer_address = None, rider = None, restaurant_list = [], food_list = [], order_state = None, payment = None) :
        self.__order_id = order_id
        self.__customer = customer
        self.__customer_address = customer_address
        self.__rider = rider
        self.__restaurant_list = restaurant_list
        self.__food_list = food_list
        self.__order_state = order_state
        self.__payment = payment
    #getter
    @property
    def order_id(self):
        return self.__order_id
    
    @property
    def customer(self):
        return self.__customer
    
    @property
    def customer_address(self):
        return self.__customer_address
    
    @property
    def rider(self):
        return self.__rider
    
    @property
    def restaurant_list(self):
        return self.__restaurant_list
    
    @property
    def food_list(self):
        return self.__food_list
    
    @property
    def order_state(self):
        return self.__order_state
    
    @property
    def payment(self):
        return self.__payment
    #setter
    @order_state.setter
    def order_state(self, new_order_state: str):
        self.__order_state = new_order_state
    