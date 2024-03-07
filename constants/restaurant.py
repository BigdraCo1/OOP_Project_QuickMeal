from internals.restaurant import Restaurant
from constants.food import *
from constants.account import *
from constants.review import *

restaurant1 = Restaurant('1',"La Piazza",
                                    "Rome",
                                    italian_dishes1,
                                    restaurant_owner_account1)

restaurant2 = Restaurant('2',"Trattoria da Luigi",
                                    "Milan",
                                    italian_dishes2,
                                    restaurant_owner_account1)

restaurant3 = Restaurant('3',"Fondue0",
                                    "Naples",
                                    italian_dishes3,
                                    restaurant_owner_account2)

restaurant4 = Restaurant('4',"KFC",
                                    "Rome",
                                    kfc_dishes,
                                    restaurant_owner_account3)