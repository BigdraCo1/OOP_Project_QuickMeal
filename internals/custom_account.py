from account import Account, Profile
class CustomerAccount(Account):
    def __init__(self, account_id: str, password: str, profile: Profile):
        if not isinstance(profile, Profile):
            ValueError("Error")
        super().__init__(account_id, password, profile)
        self.__address_list = []
        self.__reviewed_list = []

    def add_address(self, address: str):
        self.__address_list.append(address)

    def remove_address(self, address: str):
        self.__address_list.remove(address)