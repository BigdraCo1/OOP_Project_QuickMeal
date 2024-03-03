from internals.profile import Profile


class Account:
    def __init__(self, account_id: str, password: str, profile):
        self.__account_id = account_id
        self.__password = password
        self.__profile = profile

    def get_name(self):
        return self.__profile.username
    #getter
    @property
    def account_id(self):
        return self.__account_id

    @property
    def password(self):
        return self.__password

    @property
    def profile(self):
        return self.__profile
    #setter
    @account_id.setter
    def account_id(self, account_id):
        self.__account_id = account_id

    @password.setter
    def password(self, password):
        self.__password = password

    @profile.setter
    def profile(self, profile):
        self.__profile = profile
    #method
    def add_profile(self, profile):
        self.__profile = profile
        
    def search_order_by_id(self, order_id : str):
        for order in self.get_order_list():
            if order.order_id == order_id:
                print(order.order_id)
                return order
        return "Order not found"
