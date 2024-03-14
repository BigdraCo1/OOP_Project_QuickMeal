from internals.restaurant_account import RestaurantAccount
from internals.custom_account import CustomerAccount
from internals.rider_account import RiderAccount
from constants.profiles import *
from constants.pocket import *
from internals.controller import bcrypt_context
from internals.admin import Admin

restaurant_owner_account1 = RestaurantAccount(bcrypt_context.hash('Qwerty@56'), restaurant_owner_profile1,
                                              restaurant_owner_account1_pocket)


restaurant_owner_account2 = RestaurantAccount(bcrypt_context.hash('CE62@kmitl'),
                                              restaurant_owner_profile2,
                                              restaurant_owner_account2_pocket)

restaurant_owner_account3 = RestaurantAccount(bcrypt_context.hash('IZag7O1>>%'),
                                              restaurant_owner_profile3,
                                              restaurant_owner_account3_pocket)

customer_account1 = CustomerAccount(bcrypt_context.hash('password@K56'),
                                    customer_profile1,
                                    customer_account1_pocket)

customer_account2 = CustomerAccount(bcrypt_context.hash('KMitl55$uicide'),
                                    customer_profile2, 
                                    customer_account2_pocket)

rider_account1 = RiderAccount(bcrypt_context.hash('popPa%re45'),
                              rider_profile1,
                              rider_account1_pocket)

admin_account = Admin(bcrypt_context.hash('Qwerty#1234'), admin_profile, Pocket(100000000000))
