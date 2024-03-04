from internals import restaurant_account
from internals import customer_account
from internals import rider_account
from constants import profiles
from constants import pocket

restaurant_owner_account1 = restaurant_account.RestaurantAccount("Brunos",
                                                                 "5756456646",
                                                                 profiles.restaurant_owner_profile1,
                                                                 pocket.restaurant_owner_account1_pocket)


restaurant_owner_account2 = restaurant_account.RestaurantAccount("Bruno mars",
                                                                 "5756456646",
                                                                 profiles.restaurant_owner_profile2,
                                                                 pocket.restaurant_owner_account2_pocket)

restaurant_owner_account3 = restaurant_account.RestaurantAccount("Restaurant_Account_ID",
                                                                 "AccountPassword",
                                                                 profiles.restaurant_owner_profile3,
                                                                 pocket.restaurant_owner_account3_pocket)

customer_account1 = customer_account.CustomerAccount("Customer_Account_ID",
                                                     "AccountPassword",
                                                     profiles.customer_profile1,
                                                     pocket.customer_account1_pocket)

rider_account1 = rider_account.RiderAccount("Rider_Account_ID",
                                            "AccountPassword",
                                            profiles.rider_profile1,
                                            pocket.rider_account1_pocket)

