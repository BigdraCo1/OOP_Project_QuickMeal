class Account:
    def __init__(self, account_id: str, password: str, profile : object , pocket : object):
        self.__account_id = account_id
        self.__password = password
        self.__profile = profile
        self.__pocket = pocket

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
    
    @property
    def pocket(self):
        return self.__pocket
    #setter
    @account_id.setter
    def account_id(self, account_id):
        self.__account_id = account_id