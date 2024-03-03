from internals import restaurant
from constants import food, account

restaurant1 = restaurant.Restaurant('1',"La Piazza",
                                    "Rome",
                                    food.italian_dishes1,
                                    None,
                                    None,
                                    None,
                                    account.restaurant_owner_account1)

restaurant2 = restaurant.Restaurant('2',"Trattoria da Luigi",
                                    "Milan",
                                    food.italian_dishes2,
                                    None,
                                    None,
                                    None,
                                    account.restaurant_owner_account1)

restaurant3 = restaurant.Restaurant('3',"Fondue0",
                                    "Naples",
                                    food.italian_dishes3,
                                    None,
                                    None,
                                    None,
                                    account.restaurant_owner_account2)
