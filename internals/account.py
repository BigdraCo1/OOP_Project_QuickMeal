from internals.profile import Profile
from internals.pocket import Pocket


class Account:
    def __init__(self, id: str, password: str, profile: Profile = None, pocket: Pocket = None):
        self.__account_id = id
        self.__password = password
        self.__profile = profile
        self.__pocket = pocket

    def get_name(self):
        return self.__profile.username

    @property
    def account_id(self):
        return self.__account_id

    @account_id.setter
    def account_id(self, account_id):
        self.__account_id = account_id

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def profile(self):
        return self.__profile

    @profile.setter
    def profile(self, profile):
        self.__profile = profile

    @property
    def pocket(self):
        return self.__pocket

    @pocket.setter
    def pocket(self, pocket):
        self.__pocket = pocket
