from internals.account import Pocket, Profile, Account


class Admin(Account):
    def __init__(self, password: str, profile: Profile, pocket: Pocket):
        if not isinstance(profile, Profile):
            ValueError("Error")
        if not isinstance(pocket, Pocket):
            ValueError("Error")
        super().__init__('ADMIN56', password, profile, pocket)
