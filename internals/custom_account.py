from internals.account import Account, Profile


class CustomerAccount(Account) :
    def __init__(self, account_id: str, password: str, profile = None):
        super().__init__(account_id, password)
        self.__address_list = []
        self.__reviewed_list = []
        self.__current_order = []
    
    #getter
    @property
    def current_order(self):
        return self.__current_order
    
    #setter
    @current_order.setter
    def current_order(self, order):
        self.__current_order = order

    #method
    def get_order_list(self):
        return self.__current_order