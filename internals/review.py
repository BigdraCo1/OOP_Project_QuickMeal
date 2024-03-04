from internals.customer_account import CustomerAccount


class Review:
    def __init__(self, rate: int, comment: str, customer: CustomerAccount, type: str):
        self.__rate = rate
        self.__comment = comment
        self.__customer = customer
        self.__type = type