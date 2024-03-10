from internals.review import Review
from constants.account import *

review_1 = Review(5, '', customer_account1)
review_2 = Review(4, '', customer_account1)
review_3 = Review(3, '', customer_account1)
review_4 = Review(5, '', customer_account2)
review_5 = Review(2, '', customer_account2)
review_6 = Review(2, '', customer_account2)

review_list1 = [review_1, review_2, review_3]
review_list2 = [review_4, review_2, review_3, review_6]
review_list3 = [review_1, review_5, review_6, review_3, review_2]
review_list4 = [review_1, review_2, review_3, review_4, review_5, review_6]