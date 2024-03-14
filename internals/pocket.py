from internals.payment import Payment
from datetime import datetime

class Pocket:
    def __init__(self, balance = 0):
        self.__balance = balance
        self.__payment_list = []

    @property
    def balance(self):
        return self.__balance

    @property
    def payment_list(self):
        return self.__payment_list

    def add_payment(self, new_payment):
        self.__payment_list.append(new_payment)

    def top_up(self, amount):
        self.__balance += amount

    def pay_out(self, amount):
        self.__balance -= amount
