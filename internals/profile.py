from order import Order
class Profile:
    def __init__(self, username: str, telephone_number: str, email, fullname: str, balance: int):
        self.__username = username
        self.__telephone_number = telephone_number
        self.__email = email
        self.__fullname = fullname
        self.__balance = balance
        self.__order_list = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, name:str):
        self.__username = name

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, name:str):
        self.__fullname = name

    @property
    def telephone_number(self):
        return self.__fullname

    @telephone_number.setter
    def telephone_number(self, new_number: str):
        self.telephone_number = new_number

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_email: str):
        self.__email = new_email

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount: int):
        self.__balance = amount

    def pay_out(self, amount: int):
        self.__balance -= amount

    def top_up(self, amount: int):
        self.__balance += amount

