from internals import restaurant
from constants import food, account
from constants import review

restaurant1 = restaurant.Restaurant('1',"La Piazza",
                                    "Rome",
                                    food.italian_dishes1,
                                    None,
                                    None,
                                    review.review_list1,
                                    account.restaurant_owner_account1)

restaurant2 = restaurant.Restaurant('2',"Trattoria da Luigi",
                                    "Milan",
                                    food.italian_dishes2,
                                    None,
                                    None,
                                    review.review_list2,
                                    account.restaurant_owner_account1)

restaurant3 = restaurant.Restaurant('3',"Fondue0",
                                    "Naples",
                                    food.italian_dishes3,
                                    None,
                                    None,
                                    review.review_list3,
                                    account.restaurant_owner_account2)
