from internals.custom_account import CustomerAccount


class Review:
    def __init__(self, rate: int, comment: str, customer: CustomerAccount):
        self.__rate = rate
        self.__comment = comment
        self.__customer = customer

    @property
    def rate(self):
        return self.__rate
    
    @property
    def customer(self):
        return self.__customer
    
    @property
    def comment(self):
        return self.__comment
