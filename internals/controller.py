from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from starlette import status
from datetime import timedelta, datetime

from internals.custom_account import CustomerAccount, Profile, Pocket
from internals.rider_account import RiderAccount
from internals.restaurant_account import RestaurantAccount
from internals.restaurant import Restaurant
from internals.review import Review
from internals.order import Order
from internals.pocket import Pocket
from internals.payment import Payment
from internals.admin import Admin
from schema.restaurant import Restaurant_body

load_dotenv()

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


class Controller:
    def __init__(self, customer_account_list: list[CustomerAccount], rider_account_list: list[RiderAccount],
                 restaurant_account_list: list[RestaurantAccount], central_money: Pocket = None):
        self.__customer_account_list = customer_account_list
        self.__rider_account_list = rider_account_list
        self.__restaurant_account_list = restaurant_account_list
        self.__approval_rider_list: list[RiderAccount] = []
        self.__approval_restaurant_list: list[Restaurant] = []
        self.__admin = None
        self.__central_money = central_money

    @property
    def customer_account_list(self):
        return self.__customer_account_list

    @property
    def rider_account_list(self):
        return self.__rider_account_list

    @property
    def restaurant_account_list(self):
        return self.__restaurant_account_list

    @property
    def approval_rider_list(self):
        return self.__approval_rider_list

    @property
    def approval_restaurant_list(self):
        return self.__approval_restaurant_list

    @property
    def central_money(self):
        return self.__central_money

    @central_money.setter
    def central_money(self, new_central_money):
        self.__central_money = new_central_money

    # {method} add function

    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant_account(self, new_restaurant: RestaurantAccount):
        self.__restaurant_account_list.append(new_restaurant)

    # [method] remove function

    def remove_restaurant(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, Restaurant):
            restaurant_acc = restaurant.owner
            restaurant_acc.remove_restaurant(restaurant)
            del restaurant
            return 'Success'
        return 'Not Found'

    # [method] search function
    def search_customer_by_id(self, search_account_id):
        for customer in self.customer_account_list:
            if customer.account_id == search_account_id:
                return customer

    def search_rider_by_id(self, rider_id):
        for rider in self.rider_account_list:
            if rider.account_id == rider_id:
                return rider

    def search_food_by_id(self, search_food_id):
        for restaurant_acc in self.restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return food

    def search_restaurant_account_by_restaurant_id(self, search_restaurant_id):
        for restaurant_acc in self.restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                if restaurant.restaurant_id == search_restaurant_id:
                    return restaurant_acc

    def search_restaurant_by_id(self, search_restaurant_id):
        for restaurant_acc in self.restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                if restaurant.restaurant_id == search_restaurant_id:
                    return restaurant

    def search_restaurant_by_food_id(self, search_food_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return restaurant

    def search_restaurant(self, name: str):
        for restaurant_account in self.__restaurant_account_list:
            response = restaurant_account.search_restaurant(name)
            if isinstance(response, Restaurant):
                return response
        return 'Not found restaurant'

    def search_menu_and_restaurant(self, key: str):
        show_list = []
        restaurant_list = self.restaurant_account_list
        for restaurant_acc in restaurant_list:
            for restaurant in restaurant_acc.restaurant_list:
                name = restaurant.name_restaurant
                restaurant_raw_attribute = vars(restaurant)
                restaurant_attributes = {key: value for key, value in restaurant_raw_attribute.items() if
                                         key == '_Restaurant__name_restaurant'
                                         or key == '_Restaurant__restaurant_location'
                                         or key == '_Restaurant__rate'
                                         or key == '_Restaurant__restaurant_id'}
                if key.lower() in name.lower():
                    show_list.append(restaurant_attributes)
                food_list = restaurant.food_list
                for food in food_list:
                    food_name = food.name
                    if key.lower() in food_name.lower() and restaurant_attributes not in show_list:
                        show_list.append(restaurant_attributes)
        if len(show_list) < 1:
            return 'Not Found'
        return show_list

    def search_food_by_name(self, search_food_name):
        for restaurant_account in self.__restaurant_account_list:
            for restaurant in restaurant_account.restaurant_list:
                for food in restaurant.food_list:
                    if food.name == search_food_name:
                        return food

    def search_customer_current_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.current_order:
                if order.order_id == search_order_id:
                    return order

    def search_customer_order_list_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.order_list:
                if order.order_id == search_order_id:
                    return order

    def search_rider_order_by_id(self, search_order_id):
        for rider in self.__rider_account_list:
            for order in rider.receive_order_list:
                if order.order_id == search_order_id:
                    return order

    def search_restaurant_order_by_id(self, search_order_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                if (restaurant.requested_order_list) != None:
                    for order in restaurant.requested_order_list:
                        if order.order_id == search_order_id:
                            return order
                if (restaurant.request_order_list) != None:
                    for order in restaurant.request_order_list:
                        if order.order_id == search_order_id:
                            return order
                if (restaurant.finished_order_list) != None:
                    for order in restaurant.finished_order_list:
                        if order.order_id == search_order_id:
                            return order

    def search_account_from_id(self, account_id: str):
        for customer in self.__customer_account_list:
            if customer.account_id == account_id:
                return customer
        for rider in self.__rider_account_list:
            if rider.account_id == account_id:
                return rider
        for restaurant_account in self.__restaurant_account_list:
            if restaurant_account.account_id == account_id:
                return restaurant_account

    def search_restaurant_by_order_id(self, order_id: str):
        order = self.search_restaurant_order_by_id(order_id)
        restaurant = order.restaurant
        for order in restaurant.requested_order_list:
            if order.order_id == order_id:
                return restaurant
        for order in restaurant.request_order_list:
            if order.order_id == order_id:
                return restaurant
        for order in restaurant.finished_order_list:
            if order.order_id == order_id:
                return restaurant
        return "Not found restaurants"

    # [method] others function

    def get_menu_list(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, str):
            return restaurant
        return restaurant.food_list

    def edit_menu(self, restaurant, menu, request):
        acc_restaurant = self.search_restaurant(restaurant)
        if isinstance(acc_restaurant, str):
            return acc_restaurant
        return acc_restaurant.edit_menu(menu, request)

    # ====================================================

    def show_current_order(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        if not isinstance(customer, CustomerAccount):
            return f"customer_id : {customer_id} not found"
        if customer.current_order == []:
            return "No current order"
        display = []
        for order in customer.current_order:
            amount = sum(food.price for food in order.food_list)
            display.append({"order_id": order.order_id,
                            "order_state": order.order_state,
                            "order_customer": order.customer.profile.username,
                            "order_restaurant": order.restaurant.name_restaurant,
                            "food_list": [food.name for food in order.food_list],
                            "amount": amount})
        return display

    def show_order_list(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        if not isinstance(customer, CustomerAccount):
            return f"customer_id : {customer_id} not found"
        if customer.order_list == []:
            return "No current order"
        return [self.show_order_detail(order.order_id) for order in customer.order_list]

    def confirm_customer_order(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        if customer == None:
            return f"customer_id : {customer_id} not found"
        display_01 = []
        for order_lp01 in customer.current_order:
            amount = sum(food.price + food.size[food.current_size] for food in order_lp01.food_list)
            if customer.pocket.balance < amount:
                return "Insufficient balance"
            if order_lp01.customer_address == None:
                return "Address not found"
            order_lp01.order_state = "pending"
            customer.add_order_list(order_lp01)
            customer.pocket.pay_out(amount)
            self.central_money.top_up(amount)
            restaurant = order_lp01.restaurant
            restaurant.add_request_order(order_lp01)
            payment_time = datetime.now()
            payment = Payment(amount, "online", restaurant, str(payment_time.strftime("%c")), "paid", order_lp01.order_id)
            order_lp01.payment = payment
            customer.pocket.add_payment(payment)
            display_01.append({"order_id": order_lp01.order_id,
                               "order_state": order_lp01.order_state,
                               "restaurant": order_lp01.restaurant.restaurant_id,
                               "amount": order_lp01.payment.amount})
        for order_lp02 in reversed(customer.current_order):
            customer.remove_current_order(order_lp02)
        return [display_01]

    def accept_order_by_rider(self, rider_id, order_id):
        main_rider = self.search_rider_by_id(rider_id)
        if main_rider == None:
            return f"rider_id : {rider_id} not found"
        main_order = main_rider.search_request_order_by_id(order_id)
        if main_order == None:
            return f"order_id : {order_id} not found"
        if main_order.order_state != "get_res":
            return "order is not get_res"
        if main_order.order_state == "get_res":
            main_order.order_state = "get_ri"
            main_order.rider = main_rider
            restaurant = main_order.restaurant
            main_rider.add_receive_order(main_order)
            restaurant.add_requested_order(main_order)
            for rider in self.rider_account_list:
                rider.remove_request_order(main_order)
            restaurant.remove_request_order(main_order)
            return self.show_order_detail(order_id)

    def deny_order_by_rider(self, rider_id, order_id):
        main_rider = self.search_rider_by_id(rider_id)
        if main_rider == None:
            return f"rider_id : {rider_id} not found"
        main_order = main_rider.search_receive_order_by_id(order_id)
        if main_order == None:
            return f"order_id : {order_id} not found"
        if main_order.order_state != "get_ri":
            return "order is not get_ri"
        if main_order.order_state == "get_ri":
            main_order.order_state = "get_res"
            main_order.rider = None
            restaurant = main_order.restaurant
            restaurant.add_request_order(main_order)
            for rider in self.rider_account_list:
                rider.add_request_order(main_order)
            main_rider.remove_receive_order(main_order)
            restaurant.remove_requested_order(main_order)
            return self.show_order_detail(order_id)

    def receive_order_from_rider(self, rider_id, order_id):
        rider = self.search_rider_by_id(rider_id)
        if rider == None:
            return f"rider_id : {rider_id} not found"
        order = rider.search_receive_order_by_id(order_id)
        if order == None:
            return f"order_id : {order_id} not found"
        if order.order_state != "get_ri":
            return "order is not get_ri"
        order.order_state = "delivering"
        restaurant_amount = order.payment.amount * 0.8
        self.central_money.pay_out(restaurant_amount)
        restaurant = order.restaurant
        restaurant_account = self.search_restaurant_account_by_restaurant_id(restaurant.restaurant_id)
        restaurant_account.pocket.top_up(restaurant_amount)
        payment_time = datetime.now()
        payment = Payment(restaurant_amount, "online", order.restaurant, str(payment_time.strftime("%c")), "deposite", order.order_id)
        restaurant_account.pocket.add_payment(payment)
        return self.show_order_detail(order_id)

    def deliver_order(self, rider_id, order_id):
        main_rider = self.search_rider_by_id(rider_id)
        if main_rider == None:
            return f"rider_id : {rider_id} not found"
        main_order = main_rider.search_receive_order_by_id(order_id)
        if main_order == None:
            return f"order_id : {order_id} not found"
        if main_order.order_state != "delivering":
            return "order is not delivering"
        if main_order.order_state == "delivering":
            main_order.order_state = "success"
            main_rider.remove_receive_order(main_order)
            main_rider.add_finished_order(main_order)
            restaurant = main_order.restaurant
            restaurant.add_finished_order(main_order)
            restaurant.remove_requested_order(main_order)
            rider_amount = main_order.payment.amount * 0.1
            self.central_money.pay_out(rider_amount)
            main_rider.pocket.top_up(rider_amount)
            payment_time = datetime.now()
            payment = Payment(rider_amount, "online", main_order.restaurant, str(payment_time.strftime("%c")),
                              "deposite", main_order.order_id)
            main_rider.pocket.add_payment(payment)
            return self.show_order_detail(order_id)

    def show_request_order(self, rider_id):
        rider = self.search_rider_by_id(rider_id)
        if rider == None:
            return f"rider_id : {rider_id} not found"
        return [self.show_order_detail(order.order_id) for order in rider.request_order_list]

    def show_receive_order(self, rider_id):
        rider = self.search_rider_by_id(rider_id)
        if rider == None:
            return f"rider_id : {rider_id} not found"
        return [self.show_order_detail(order.order_id) for order in rider.receive_order_list]

    def show_finished_order(self, rider_id):
        rider = self.search_rider_by_id(rider_id)
        if rider == None:
            return f"rider_id : {rider_id} not found"
        return [self.show_order_detail(order.order_id) for order in rider.finished_order_list]

    def remove_menu(self, restaurant, menu):
        real_restaurant = self.search_restaurant(restaurant)
        if isinstance(real_restaurant, str):
            return real_restaurant
        return real_restaurant.remove_food(menu)

    def new_menu(self, restaurant, request):
        real_restaurant = self.search_restaurant(restaurant)
        if isinstance(real_restaurant, str):
            return None
        return real_restaurant.add_menu(request)


    def show_restaurant(self):
        show_list = []
        restaurant_list = self.restaurant_account_list
        for restaurant_acc in restaurant_list:
            for restaurant in restaurant_acc.restaurant_list:
                restaurant_raw_attribute = vars(restaurant)
                restaurant_attributes = {key: value for key, value in restaurant_raw_attribute.items() if
                                         key == '_Restaurant__name_restaurant'
                                         or key == '_Restaurant__restaurant_location'
                                         or key == '_Restaurant__rate'
                                         or key == '_Restaurant__restaurant_id'}
                show_list.append(restaurant_attributes)
        return show_list

    def show_restaurant_menu(self, restaurant_id):
        food_dict = {}
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for food in restaurant.food_list:
            food_dict[food.id] = [food.name, food.price]
        return food_dict

    def calculate_total_of_basket(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        basket = customer.current_order
        total = 0
        for order in basket:
            for food in order.food_list:
                total += food.price + food.size[food.current_size]
        return total

    def show_basket(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        basket = customer.current_order
        basket_dict = {}
        if basket != []:
            basket_dict["total"] = self.calculate_total_of_basket(customer_id)
            basket_dict["address"] = basket[0].customer_address
            for order in basket:
                already_add = []
                for food in order.food_list:
                    if food not in already_add:
                        quantity = len(
                            [f for f in order.food_list if (f.id == food.id and f.current_size == food.current_size)])
                        basket_dict[f"id-{food.id} {food.current_size}"] = [
                            quantity, food.id, food.name, food.price + food.size[str(food.current_size)], food.current_size]
                        already_add.append(food)
        return basket_dict

    def show_address(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        return [address for address in customer.address_list]

    def add_address_to_basket(self, customer_id, address):
        customer = self.search_customer_by_id(customer_id)
        basket = customer.current_order
        if address not in customer.address_list:
            customer.add_address(address)
        for order in basket:
            order.customer_address = address
        return f"{address} is now set as address of your order"

    def show_food_detail(self, food_id):
        food = self.search_food_by_id(food_id)
        return {"food_id": food.id,
                "food_name": food.name,
                "food_type": food.type,
                "food_size": food.size,
                "food_price": food.price}

    def add_food_to_basket(self, customer_id, food_id, size, quantity):
        customer = self.search_customer_by_id(customer_id)
        food = self.search_food_by_id(food_id)
        restaurant = self.search_restaurant_by_food_id(food_id)
        customer.add_food(food, size, quantity, restaurant)
        return f"{quantity} x {size} {food.name} is added to your basket!"

    def change_quantity(self, customer_id, food_id, quantity, new_quantity, size):
        customer = self.search_customer_by_id(customer_id)
        food = self.search_food_by_id(food_id)
        restaurant = self.search_restaurant_by_food_id(food_id)
        customer.remove_food(food_id, size, quantity, restaurant)
        if new_quantity > 0:
            customer.add_food(food, size, new_quantity, restaurant)
            return f"{size} {food.name} is now {new_quantity}"
        else:
            for order in customer.current_order:
                if order.restaurant == restaurant:
                    if order.food_list != []:
                        return f"{size} {food.name} is remove from basket"
                    customer.current_order.remove(order)
                    return f"{size} {food.name} is remove from basket"

    # ถ้ามาพร้อม change_quantity ให้ change_quantity ก่อน
    def change_size(self, customer_id, food_id, size, new_size):
        customer = self.search_customer_by_id(customer_id)
        basket = customer.current_order
        food = self.search_food_by_id(food_id)
        for order in basket:
            for customer_food in order.food_list:
                if customer_food.id == food.id and customer_food.current_size == size:
                    customer_food.current_size = new_size
        return f"{size} {food.name} is now {new_size}"

    def show_review(self, restaurant_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant.reviewed_list == []:
            return {}
        else:
            dct = {}
            for review in restaurant.reviewed_list:
                dct[f"{review.customer.get_name()}"] = [review.rate, review.comment]
        return dct

    def add_review_to_restaurant(self, customer_id, rating, comment, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if not (0 <= rating <= 5):
            raise ValueError('rating value is between 0 to 5')
        for review in restaurant.reviewed_list:
            if review.customer == customer:
                restaurant.reviewed_list.remove(review)
                customer.reviewed_list.remove(review)
                del review
        for order in customer.order_list:
            if order.restaurant.restaurant_id == restaurant.restaurant_id:
                review = Review(rating, comment, customer)
                customer.add_review(review)
                restaurant.add_review(review)
                return f"you have writing a review to {restaurant.name_restaurant}"
        return f"you've never ordered food from {restaurant.name_restaurant}"

    def remove_review_from_restaurant(self, customer_id, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for review in restaurant.reviewed_list:
            if review.customer == customer:
                restaurant.reviewed_list.remove(review)
                customer.reviewed_list.remove(review)
                del review
        return f"you have remove a review from {restaurant.name_restaurant}"


    def change_order_state(self, order: Order, order_state: str):
        order.order_state = order_state
        return "Order state changed"

    def customer_cancel_order(self, customer_account_id: str, order_id: str):
        customer_account = self.search_account_from_id(customer_account_id)
        if not isinstance(customer_account, CustomerAccount):
            return "Account is not customer account"
        if self.search_customer_order_list_by_id(order_id) == None:
            return "Order not found"
        order = self.search_customer_order_list_by_id(order_id)
        restaurant = self.search_restaurant_by_order_id(order_id)
        order_state = order.order_state
        if self.check_order_state(order_state) != None:
            return self.check_order_state(order_state)
        order.change_payment_status("Refunded")
        self.change_order_state(order, "Cancelled by Customer")
        customer_account.pocket.add_payment(order.payment)
        if (isinstance(order.rider, RiderAccount)):
            order.rider.add_finished_order(order)
            order.rider.remove_receive_order(order)
            order.rider.pocket.add_payment(order)
            order.rider.pocket.add_payment(
                Payment(order.payment.amount * 0.1, "online", order.rider, str(datetime.now().strftime("%c")), "Cancel",
                        order.order_id))

        order.restaurant.add_finished_order(order)
        if (isinstance(order.restaurant, Restaurant)):
            restaurant_account = self.search_restaurant_account_by_restaurant_id(restaurant.restaurant_id)
            if order in order.restaurant.requested_order_list:
                order.restaurant.remove_requested_order(order)
                order.restaurant.add_finished_order(order)
            if order in order.restaurant.request_order_list:
                order.restaurant.remove_request_order(order)
                order.restaurant.add_finished_order(order)
            restaurant_account.pocket.add_payment(
                Payment(order.payment.amount * 0.8, "online", order.restaurant, str(datetime.now().strftime("%c")),
                        "Cancel", order.order_id))
        total = 0
        for food in order.food_list:
            total += food.price + food.size[food.current_size]
        order.customer.pocket.top_up(total)
        return customer_account_id + " Order ID : " + order_id + " is cancelled. Payment is refunded."

    def rider_cancel_order(self, rider_account_id: str, order_id: str):
        rider_account = self.search_account_from_id(rider_account_id)
        if not isinstance(rider_account, RiderAccount):
            return "Account is not rider account"
        order = self.search_rider_order_by_id(order_id)
        restaurant = self.search_restaurant_by_order_id(order_id)
        order_state = order.order_state
        if self.check_order_state(order_state) != None:
            return self.check_order_state(order_state)
        order.change_payment_status("Refunded")
        self.change_order_state(order, "Cancelled by Rider")
        rider_account.pocket.add_payment(order.payment)
        if (isinstance(order.rider, RiderAccount)):
            order.rider.add_finished_order(order)
            order.rider.remove_receive_order(order)
        order.restaurant.add_finished_order(order)
        order.restaurant.remove_requested_order(order)
        total = 0
        for food in order.food_list:
            total += food.price + food.size[food.current_size]
        order.customer.pocket.top_up(total)
        restaurant_account = self.search_restaurant_account_by_restaurant_id(restaurant.restaurant_id)
        restaurant_account.pocket.add_payment(Payment(order.payment.amount * 0.8, "online", order.restaurant, str(datetime.now().strftime("%c")), "Cancel", order.order_id))
        order.rider.pocket.add_payment(Payment(order.payment.amount * 0.1, "online", order.rider, str(datetime.now().strftime("%c")), "Cancel", order.order_id))
        return rider_account_id + " Order ID : " + order_id + " is cancelled."

    def restaurant_cancel_order(self, restaurant_id: str, order_id: str, food_name: str):
        food = None
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if self.search_restaurant_order_by_id(order_id) == None:
            return "Order not found"
        order = self.search_restaurant_order_by_id(order_id)
        if self.search_food_by_name(food_name) == None:
            return "Food not found."
        total = 0
        for food_inlist in order.food_list:
            if food_inlist.name == food_name:
                food = food_inlist
                total += food_inlist.price + food_inlist.size[food_inlist.current_size]
        order_state = order.order_state
        if self.check_order_state(order_state) != None:
            return self.check_order_state(order_state)
        order.remove_food_from_order_by_name(food.name)
        self.change_order_state(order, order_state + "\n" + food_name + " Cancelled : " )
        order.customer.pocket.top_up(total)
        order.change_payment_status(order.payment.payment_status + " Food : " + food_name + " is Refunded")
        if order.food_list == []:
            self.change_order_state(order, "Cancelled by Restaurant.")
            order.rider.add_finished_order(order)
            order.rider.remove_receive_order(order)
            order.restaurant.add_finished_order(order)
            order.restaurant.remove_requested_order(order)
            order.change_payment_status("Refunded")
            restaurant_account = self.search_restaurant_account_by_restaurant_id(restaurant.restaurant_id)
            restaurant_account.pocket.add_payment(Payment(order.payment.amount * 0.8, "online", order.restaurant, str(datetime.now().strftime("%c")), "Cancel", order.order_id))
            order.rider.pocket.add_payment(Payment(order.payment.amount * 0.1, "online", order.rider, str(datetime.now().strftime("%c")), "Cancel", order.order_id))
            return restaurant_id + " Order ID : " + order_id + " is cancelled."
        return restaurant_id + " " + food_name + " in " + order_id + " is refund."

    # [method] order function

    def show_order_detail(self, order_id: str):
        order_detail = dict()
        if self.search_customer_order_list_by_id(order_id) != None:
            order = self.search_customer_order_list_by_id(order_id)
        elif self.search_customer_current_order_by_id(order_id) != None:
            order = self.search_customer_current_order_by_id(order_id)
        else:
            order_detail["Order_Not_Found"] = order_id + " is not found in list"
            return order_detail
        if not isinstance(order, Order):
            return order
        order_detail["Order_ID"] = order.order_id
        order_detail["Customer"] = order.customer.profile.username
        if isinstance(order.rider, RiderAccount):
            order_detail["Rider"] = order.rider.profile.username
        else:
            order_detail["Rider"] = "No rider_id"
        order_detail["Restaurant"] = order.restaurant.name_restaurant
        food_list = []
        for food in order.food_list:
            food_list.append(f"{food.current_size} {food.name} {food.price+food.size[food.current_size]}")
        order_detail["Food"] = food_list
        order_detail["Order_State"] = order.order_state
        if isinstance(order.payment, Payment):
            order_detail["Payment"] = order.payment.payment_status
        else:
            order_detail["Payment"] = "No payment"
        return order_detail

    def show_pocket_detail(self, account_id: str):
        pocket_detail = dict()
        if self.search_account_from_id(account_id) == None:
            pocket_detail["Account_Not_Found"] = account_id + " is not found in list"
            return pocket_detail
        account = self.search_account_from_id(account_id)
        pocket = account.pocket
        pocket_detail["Account_ID"] = account_id
        pocket_detail["Balance"] = pocket.balance
        return pocket_detail

    def show_payment_detail(self, account_id: str):
        account = self.search_account_from_id(account_id)
        payment_dict = dict()
        if self.search_account_from_id(account_id) == None:
            payment_dict["Account_Not_Found"] = account_id + " is not found in list"
            return payment_dict
        if isinstance(account, RestaurantAccount):
            for payment in account.pocket.payment_list:
                payment_dict[payment.transaction_id] = [payment.order_id, payment.payment_status, payment.amount]
        elif isinstance(account, CustomerAccount):
            for payment in account.pocket.payment_list:
                payment_dict[payment.transaction_id] = [payment.order_id, payment.payment_status, payment.amount]
        elif isinstance(account, RiderAccount):
            for payment in account.pocket.payment_list:
                payment_dict[payment.transaction_id] = [payment.order_id, payment.payment_status, payment.amount]
        return payment_dict

    def check_order_state(self, order_state: str):
        if order_state == "delivering":
            return "Cant cancel order, rider is delivering"
        if order_state == "Cancelled by Customer":
            return "Order already cancelled by customer"
        if order_state == "Cancelled by Rider":
            return "Order already cancelled by rider"
        if order_state == "Cancelled by Restaurant":
            return "Order already cancelled by restaurant"
        if order_state == "Success":
            return "Order already success"

    def accept_order_by_restaurant(self, restaurant_id, order_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant == None:
            return f"restaurant_id : {restaurant_id} not found"
        order = restaurant.search_request_order_by_id(order_id)
        if order == None:
            return f"order_id : {order_id} not found"
        if order.order_state != "pending":
            return "order is not pending"
        order.order_state = "get_res"
        for rider in self.rider_account_list:
            rider.add_request_order(order)
        return self.show_order_detail(order_id)

    def deny_order_by_restaurant(self, restaurant_id, order_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant == None:
            return f"restaurant_id : {restaurant_id} not found"
        order = restaurant.search_request_order_by_id(order_id)
        if order == None:
            return f"order_id : {order_id} not found"
        if order.order_state != "get_res":
            return "order is not get_res"
        order.order_state = "denied_by_restaurant"
        order.payment.payment_status = "Refund"
        restaurant.remove_request_order(order)
        for rider in self.rider_account_list:
            rider.remove_request_order(order)
        customer = order.customer
        pay_back_amount = order.payment.amount
        self.central_money.pay_out(pay_back_amount)
        customer.pocket.top_up(pay_back_amount)
        return self.show_order_detail(order_id)

    def add_customer_account_by_request(self, password, username, telephone_number, email, fullname):
        account_list = self.restaurant_account_list + self.customer_account_list + self.rider_account_list
        for acc in account_list:
            if acc.get_name() == username:
                return "This username has been used"
            if acc.profile.email == email or acc.profile.telephone_number == telephone_number:
                return "Your data has been used"
        new_customer = CustomerAccount(password, Profile(username, telephone_number, email, fullname), Pocket(0))
        self.__customer_account_list.append(new_customer)
        customer_attribute = vars(new_customer)
        return {key: value for key, value in customer_attribute.items() if
                key == '_Account__account_id' or key == '_Account__profile' or key == '_Account__password'}

    def add_restaurant_account_by_request(self, password, username, telephone_number, email, fullname):
        account_list = self.restaurant_account_list + self.customer_account_list + self.rider_account_list
        for acc in account_list:
            if acc.get_name() == username:
                return "This username has been used"
            if acc.profile.email == email or acc.profile.telephone_number == telephone_number:
                return "Your data has been used"
        new_restaurant_account = RestaurantAccount(password, Profile(username, telephone_number, email, fullname),
                                                   Pocket(0))
        self.__restaurant_account_list.append(new_restaurant_account)
        new_restaurant_account_attribute = vars(new_restaurant_account)
        return {key: value for key, value in new_restaurant_account_attribute.items() if
                key != '_Account__pocket' and key != '_RestaurantAccount__restaurant_list'}

    def add_rider_account_by_request(self, password, username, telephone_number, email, fullname):
        account_list = self.restaurant_account_list + self.customer_account_list + self.rider_account_list + self.approval_rider_list
        for acc in account_list:
            if acc.get_name() == username:
                return "This username has been used"
            if acc.profile.email == email or acc.profile.telephone_number == telephone_number:
                return "Your data has been used"
        new_rider_account = RiderAccount(password, Profile(username, telephone_number, email, fullname),
                                         Pocket(0))
        self.approval_rider_list.append(new_rider_account)
        new_rider_account_attribute = vars(new_rider_account)
        return {key: value for key, value in new_rider_account_attribute.items() if
                key == '_Account__account_id' or key == '_Account__profile' or key == '_Account__password'}

    def search_instance_by_name(self, username):
        if username == self.admin.get_name():
            return self.__admin
        for customer in self.customer_account_list:
            if customer.get_name() == username:
                return customer
        for restaurant_acc in self.restaurant_account_list:
            if restaurant_acc.get_name() == username:
                return restaurant_acc
        for rider in self.rider_account_list:
            if rider.get_name() == username:
                return rider
        return False

    def assign_admin(self, admin: Admin):
        if isinstance(admin, Admin):
            self.__admin = admin
            return {'detail':'Success'}
        return {'detail' :'You are not Admin'}

    @property
    def admin(self):
        return self.__admin

    def check_access_restaurant_by_restaurant_name(self, username: str, restaurant_name: str):
        instance = self.search_instance_by_name(username)
        if isinstance(instance, RestaurantAccount):
            for restaurant in instance.restaurant_list:
                if restaurant.name_restaurant == restaurant_name:
                    return True
        return False

    def check_access_restaurant_by_restaurant_id(self, username: str, restaurant_id: str):
        instance = self.search_instance_by_name(username)
        if isinstance(instance, RestaurantAccount):
            for restaurant in instance.restaurant_list:
                if restaurant.restaurant_id == restaurant_id:
                    return True
        return False


    def check_access_customer_by_id(self, user_id: str, customer_id):
        if user_id != customer_id:
            return False
        return True


    def check_access_rider_by_id(self, user_id: str, rider_id):
        if user_id != rider_id:
            return False
        return True

    def check_access_restaurant_acc_by_id(self, user_id: str, restaurant_acc_id):
        if user_id != restaurant_acc_id:
            return False
        return True

    def show_rider_approval_list(self):
        show_list = []
        for rider in self.approval_rider_list:
            rider_attribute = {'account_id': rider.account_id, 'profile': rider.profile}
            show_list.append(rider_attribute)
        return show_list

    def show_restaurant_approval_list(self):
        show_list = []
        for restaurant in self.approval_restaurant_list:
            restaurant_attribute = {'restaurant_id': restaurant.restaurant_id, 'name': restaurant.name_restaurant,
                                    'location': restaurant.restaurant_location}
            show_list.append(restaurant_attribute)
        return show_list

    def remove_restaurant_in_approve_list(self, restaurant_name: str):
        for restaurant in self.approval_restaurant_list:
            if restaurant.name_restaurant == restaurant_name:
                self.approval_restaurant_list.remove(restaurant)
                del restaurant
                return 'Success'
        return 'Not Found'

    def remove_rider_in_approve_list(self, rider_username: str):
        for rider in self.approval_rider_list:
            if rider.get_name() == rider_username:
                self.approval_rider_list.remove(rider)
                del rider
                return 'Success'
        return 'Not Found'

    def approve_rider(self, rider_username: str):
        for rider in self.approval_rider_list:
            if rider.get_name() == rider_username:
                self.add_rider_account(rider)
                self.approval_rider_list.remove(rider)
                return 'Success'
        return 'Not Found'

    def approve_restaurant(self, restaurant_name: str):
        for restaurant in self.approval_restaurant_list:
            if restaurant.name_restaurant == restaurant_name:
                for restaurant_acc in self.restaurant_account_list:
                    if restaurant_acc == restaurant.owner:
                        restaurant_acc.assign_restaurant(restaurant)
                        self.approval_restaurant_list.remove(restaurant)
                        return 'Success'
        return 'Not Found'

    def new_restaurant(self, username: str, request: Restaurant_body):
        for restaurant in self.approval_restaurant_list:
            if restaurant.name_restaurant == request.name_restaurant:
                return 'This name was taken'
        if isinstance(self.search_restaurant(request.name_restaurant), Restaurant):
            return 'This name was taken'
        for restaurant_acc in self.restaurant_account_list:
            if restaurant_acc.get_name() == username:
                restaurant = Restaurant(request.name_restaurant, request.restaurant_location, [], [], [], [],
                                        restaurant_acc)
                self.approval_restaurant_list.append(restaurant)
                return 'Success'
        return 'Not Found'

    def show_restaurant_detail_by_id(self, restaurant_id: str):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        restaurant_detail = dict()
        if not isinstance(restaurant, Restaurant):
            return restaurant
        restaurant_detail["Restaurant_ID"] = restaurant.restaurant_id
        restaurant_detail["Restaurant_Name"] = restaurant.name_restaurant
        restaurant_detail["Restaurant_Location"] = restaurant.restaurant_location
        restaurant_detail["Rate"] = restaurant.rate
        return restaurant_detail

    def show_restaurant_by_restaurant_account_id(self, restaurant_account_id: str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        if not isinstance(restaurant_account, RestaurantAccount):
            return "Account is not restaurant account"
        restaurant_dict = dict()
        restaurant_list = list()
        for restaurant in restaurant_account.restaurant_list:
            restaurant_list.append(self.show_restaurant_detail_by_id(restaurant.restaurant_id))
        restaurant_dict[restaurant_account_id] = restaurant_list
        return restaurant_dict

    def show_account_profile(self, account_id: str):
        account = self.search_account_from_id(account_id)
        account_profile = dict()
        if not isinstance(account, CustomerAccount) and not isinstance(account, RiderAccount) and not isinstance(account, RestaurantAccount):
            return "Account not found"
        account_profile["Username"] = account.profile.username
        account_profile["Fullname"] = account.profile.fullname
        account_profile["Email"] = account.profile.email
        account_profile["Phone"] = account.profile.telephone_number
        account_profile["ID"] = account.account_id
        return account_profile

    def show_restaurant_detail_by_name(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        restaurant_detail = dict()
        if not isinstance(restaurant, Restaurant):
            return restaurant
        restaurant_detail["Restaurant_Name"] = restaurant.name_restaurant
        restaurant_detail["Restaurant_Location"] = restaurant.restaurant_location
        restaurant_detail["Rate"] = restaurant.rate
        restaurant_detail["Restaurant_ID"] = restaurant.restaurant_id
        return restaurant_detail

    def show_request_order_list_in_restaurant(self, restaurant_id: str):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        request_order_dict = dict()
        order_detail_list = list()
        for request_order in restaurant.request_order_list:
            order_detail_list.append(self.show_order_detail(request_order.order_id))
        request_order_dict[restaurant.name_restaurant] = order_detail_list
        return request_order_dict

    def show_requested_order_list_in_restaurant(self, restaurant_id: str):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        requested_order_dict = dict()
        order_detail_list = list()
        for requested_order in restaurant.requested_order_list:
            order_detail_list.append(self.show_order_detail(requested_order.order_id))
        requested_order_dict[restaurant.name_restaurant] = order_detail_list
        return requested_order_dict

    def show_finished_order_list_in_restaurant(self, restaurant_id: str):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        finish_order_dict = dict()
        order_detail_list = list()
        for finished_order in restaurant.finished_order_list:
            order_detail_list.append(self.show_order_detail(finished_order.order_id))
        finish_order_dict[restaurant.name_restaurant] = order_detail_list
        return finish_order_dict

    def show_food_in_order(self, order_id: str):
        order = None
        if self.search_customer_order_list_by_id(order_id) != None:
            order = self.search_customer_order_list_by_id(order_id)
        elif self.search_customer_current_order_by_id(order_id) != None:
            order = self.search_customer_current_order_by_id(order_id)
        food_dict = dict()
        food_list = list()
        for food in order.food_list:
            food_list.append(self.show_food_detail(food.id))
        food_dict[order_id] = food_list
        return food_dict

    def get_menu(self, restaurant_name: str , menu_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, str):
            return restaurant
        for food in restaurant.food_list:
            if menu_name == food.name:
                return food
        return 'Not Found'

    def delete_address(self, customer_id, address):
        customer = self.search_customer_by_id(customer_id)
        if address in customer.address_list:
            customer.remove_address(address)
        return f"{address} is now remove from your address"

    def topup_pocket(self, id, amount):
        account = None
        if (self.search_account_from_id(id) != None):
            account = self.search_account_from_id(id)
        elif (self.search_restaurant_by_id(id) != None):
            account = self.search_restaurant_by_id(id)
        elif (self.search_rider_by_id(id) != None):
            account = self.search_rider_by_id(id)
        else:
            return account
        account.pocket.top_up(amount)
        return f"your pocket is now {account.pocket.balance} baht"

    def authenticate_user(self, username: str, password: str):
        user = self.search_instance_by_name(username)
        if user is None:
            return False
        if not bcrypt_context.verify(password, user.password):
            return False
        return user

    def create_access_token(self, username: str, user_id: int, expires_delta: timedelta):
        user_role = ''
        if not (self.admin is None):
            user_role = 'admin'
        if isinstance(self.search_instance_by_name(username), CustomerAccount):
            user_role = 'customer'
        if isinstance(self.search_instance_by_name(username), RestaurantAccount):
            user_role = 'restaurant'
        if isinstance(self.search_instance_by_name(username), RiderAccount):
            user_role = 'rider'
        encode = {'sub': username, 'id': user_id, 'role': user_role}
        expires = datetime.utcnow() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

    async def get_current_customer(self, token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get('sub')
            user_id: str = payload.get('id')
            user_role: str = payload.get('role')
            if username is None or user_id is None or (user_role != 'customer' and user_role != 'admin'):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
            return {'username': username, 'id': user_id, 'role': user_role}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')

    async def get_current_restaurant(self, token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get('sub')
            user_id: str = payload.get('id')
            user_role: str = payload.get('role')
            if username is None or user_id is None or (user_role != 'restaurant' and user_role != 'admin'):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
            return {'username': username, 'id': user_id, 'role': user_role}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')

    async def get_current_admin(self, token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get('sub')
            user_id: str = payload.get('id')
            user_role: str = payload.get('role')
            if username is None or user_id is None or user_role != 'admin':
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
            return {'username': username, 'id': user_id, 'role': user_role}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')

    async def get_current_rider(self ,token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get('sub')
            user_id: str = payload.get('id')
            user_role: str = payload.get('role')
            if username is None or user_id is None or (user_role != 'rider' and user_role != 'admin'):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
            return {'username': username, 'id': user_id, 'role': user_role}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')

    async def get_current_account(self, token: Annotated[str, Depends(oauth2_bearer)]):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get('sub')
            user_id: str = payload.get('id')
            user_role: str = payload.get('role')
            if username is None or user_id is None or (
                    user_role != 'rider' and user_role != 'restaurant' and user_role != 'customer' and user_role != 'admin'):
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')
            return {'username': username, 'id': user_id, 'role': user_role}
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate')


    def get_restaurant_owner_id_by_restaurant_name(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        for restaurant_acc in self.restaurant_account_list:
            for restaurant_in_acc in restaurant_acc.restaurant_list:
                if restaurant_in_acc == restaurant:
                    return {"restaurant_owner": restaurant_acc.account_id}