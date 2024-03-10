from internals.restaurant import Restaurant
from constants.food import *
from constants.account import *
from constants.review import *

restaurant1 = Restaurant("La Piazza",
                                    "Rome",
                                    italian_dishes1,
                                    [],
                                    [],
                                    review_list1,
                                    restaurant_owner_account1)

restaurant2 = Restaurant("Trattoria da Luigi",
                                    "Milan",
                                    italian_dishes2,
                                    [],
                                    [],
                                    review_list2,
                                    restaurant_owner_account1)

restaurant3 = Restaurant("Fondue0",
                                    "Naples",
                                    italian_dishes3,
                                    [],
                                    [],
                                    review_list3,
                                    restaurant_owner_account2)

restaurant4 = Restaurant("KFC",
                                    "Rome",
                                    kfc_dishes,
                                    [],
                                    [],
                                    review_list4,
                                    restaurant_owner_account3)