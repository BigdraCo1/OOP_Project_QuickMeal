from internals.restaurant_account import RestaurantAccount
from internals.custom_account import CustomerAccount
from internals.rider_account import RiderAccount
from constants.profiles import *
from constants.pocket import *

restaurant_owner_account1 = RestaurantAccount("Brunos",
                                              "5756456646",
                                              restaurant_owner_profile1,
                                              restaurant_owner_account1_pocket)


restaurant_owner_account2 = RestaurantAccount("Bruno mars",
                                              "5756456646",
                                              restaurant_owner_profile2,
                                              restaurant_owner_account2_pocket)

restaurant_owner_account3 = RestaurantAccount("707",
                                              "AccountPassword",
                                              restaurant_owner_profile3,
                                              restaurant_owner_account3_pocket)

customer_account1 = CustomerAccount("101",
                                    "601",
                                    customer_profile1,
                                    customer_account1_pocket)

customer_account2 = CustomerAccount("102", 
                                    "602", 
                                    customer_profile2, 
                                    customer_account2_pocket)

rider_account1 = RiderAccount("201", 
                              "801",
                              rider_profile1,
                              rider_account1_pocket)