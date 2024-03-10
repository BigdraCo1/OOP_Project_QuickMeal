from internals.food import Food


class Order:
    ID = 1
    def __init__(self, customer=None, customer_address=None, rider=None, restaurant=None,
                 food_list=[], order_state=None, payment=None):
        self.__order_id = f"O{Order.ID}"
        Order.ID += 1
        self.__customer = customer
        self.__customer_address = customer_address
        self.__rider = rider
        self.__restaurant = restaurant
        self.__food_list = food_list
        self.__order_state = order_state
        self.__payment = payment

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
    
    @rider.setter
    def rider(self, new_rider):
        self.__rider = new_rider

    @property
    def restaurant(self):
        return self.__restaurant

    @property
    def food_list(self):
        return self.__food_list

    @property
    def order_state(self):
        return self.__order_state

    @property
    def payment(self):
        return self.__payment

    @order_state.setter
    def order_state(self, new_order_state: str):
        self.__order_state = new_order_state
        
    @payment.setter
    def payment(self, new_payment):
        self.__payment = new_payment

    @restaurant.setter
    def restaurant(self, new_restaurant):
        self.__restaurant = new_restaurant

    @customer_address.setter
    def customer_address(self, new_customer_address):
        self.__customer_address = new_customer_address

    # method
    def change_payment_status(self, status: str):
        self.__payment.payment_status = status

    def remove_food_from_order(self, food: Food):
        self.__food_list.remove(food)