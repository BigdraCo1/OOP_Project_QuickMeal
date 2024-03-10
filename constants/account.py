from internals.restaurant_account import RestaurantAccount
from internals.custom_account import CustomerAccount
from internals.rider_account import RiderAccount
from constants.profiles import *
from constants.pocket import *
from utils.dependencies import bcrypt_context
from internals.admin import Admin

restaurant_owner_account1 = RestaurantAccount(bcrypt_context.hash('edhbejhdbw'), restaurant_owner_profile1,
                                              restaurant_owner_account1_pocket)


restaurant_owner_account2 = RestaurantAccount(bcrypt_context.hash('edhvrefbejhdbw'),
                                              restaurant_owner_profile2,
                                              restaurant_owner_account2_pocket)

restaurant_owner_account3 = RestaurantAccount(bcrypt_context.hash('edhbrefwerdfeejhdbw'),
                                              restaurant_owner_profile3,
                                              restaurant_owner_account3_pocket)

customer_account1 = CustomerAccount(bcrypt_context.hash('edhbejrferhdbw'),
                                    customer_profile1,
                                    customer_account1_pocket)

customer_account2 = CustomerAccount(bcrypt_context.hash('edhbejrfvcervhdbw'),
                                    customer_profile2, 
                                    customer_account2_pocket)

rider_account1 = RiderAccount(bcrypt_context.hash('edhefvcervcbejhdbw'),
                              rider_profile1,
                              rider_account1_pocket)

admin_account = Admin(bcrypt_context.hash('qwerty1234'), admin_profile, Pocket(100000000000))
