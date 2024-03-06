from internals.account import Account, Profile


class CustomerAccount(Account):
    def __init__(self, account_id: str, password: str, profile: Profile):
        if not isinstance(profile, Profile):
            ValueError("Error")
        super().__init__(account_id, password, profile)
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

    def add_address(self, address: str):
        self.__address_list.append(address)

    def remove_address(self, address: str):
        self.__address_list.remove(address)
        
    def search_order_by_id(self, order_id):
        for order in self.__order_cart:
            if order.order_id == order_id: return order
        return None