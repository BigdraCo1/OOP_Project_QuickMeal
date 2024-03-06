from datetime import datetime
from internals.payment import Payment

class Pocket: 
    def __init__(self, balance):
        self.__balance = balance
        self.__payment_list = []
    
    @property    
    def balance(self):
        return self.__balance
    
    def add_payment(self, new_payment):
        self.__payment_list.append(new_payment)
        
    def top_up(self, amount):
        self.__balance += amount
        
    def pay_out(self, amount):
        self.__balance -= amount
    
    def deposite(self, amount):
        self.__balance += amount
        self.__payment_list.append(Payment("deposite", datetime.now(), amount))
        
    def withdraw(self, amount):
        self.__balance -= amount
        self.__payment_list.append(Payment("withdraw", datetime.now(), amount))
