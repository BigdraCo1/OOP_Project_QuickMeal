from internals.account import Account
from internals.rider_account import RiderAccount
from internals.restaurant_account import RestaurantAccount
from internals.customer_account import CustomerAccount
from internals.restaurant import Restaurant
from internals.order import Order
from internals.food import Food


class Controller:
    def __init__(self, customer_account_list: list[CustomerAccount], rider_account_list: list[RiderAccount],
                 restaurant_account_list: list[RestaurantAccount]):
        self.__customer_account_list = customer_account_list
        self.__rider_account_list = rider_account_list
        self.__restaurant_account_list = restaurant_account_list
        self.__approval_list = None

    @property
    def customer_account_list(self):
        return self.__customer_account_list

    @property
    def rider_account_list(self):
        return self.__rider_account_list

    @property
    def restaurant_list(self):
        return self.__restaurant_account_list
    
    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant_account(self, new_restaurant: RestaurantAccount):
        self.__restaurant_account_list.append(new_restaurant)

    def remove_customer_account(self, customer: CustomerAccount):
        self.__customer_account_list.remove(customer)
        del customer

    def remove_rider_account(self, rider: RiderAccount):
        self.__rider_account_list.remove(rider)
        del rider

    def remove_rider_account(self, rider: RiderAccount):
        self.__rider_account_list.remove(rider)
        del rider

    def remove_restaurant(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, Restaurant):
            restaurant_acc = restaurant.owner
            restaurant_acc.remove_restaurant(restaurant)
            del restaurant
            return 'Success'
        return 'Not Found'

    def search_restaurant(self, name: str):
        for restaurant_account in self.__restaurant_account_list:
            response = restaurant_account.search_restaurant(name)
            if isinstance(response, Restaurant):
                return response
        return 'Not found restaurant'

    def get_menu_list(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, str):
            return restaurant
        return restaurant.food_list
    
    def search_menu_and_restaurant(self, key: str):
        show_list = []
        restaurant_list = self.restaurant_list
        for restaurant_acc in restaurant_list:
            for restaurant in restaurant_acc.restaurant_list:
                name = restaurant.restaurant_name
                restaurant_raw_attribute = vars(restaurant)
                restaurant_attributes = {key: value for key, value in restaurant_raw_attribute.items() if
                                         key != '_Restaurant__owner'}
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
    
    def edit_menu(self, restaurant, menu, request):
        acc_restaurant = self.search_restaurant(restaurant)
        if isinstance(acc_restaurant, str):
            return acc_restaurant
        return acc_restaurant.edit_menu(menu, request)

    def remove_menu(self, restaurant, menu):
        real_restaurant = self.search_restaurant(restaurant)
        if isinstance(real_restaurant, str):
            return real_restaurant
        return real_restaurant.remove_food(menu)
    
    def search_current_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            if customer.current_order.order_id == search_order_id:
                return customer.current_order

    def new_menu(self, restaurant, request):
        real_restaurant = self.search_restaurant(restaurant)
        return real_restaurant.add_menu(request)
    
    def search_customer_by_id(self, search_account_id):
        for customer in self.__customer_account_list:
            if customer.account_id == search_account_id:
                return customer
    
    def search_food_by_id(self, search_food_id):
        for restaurant_account in self.__restaurant_account_list:
            for restaurant in restaurant_account.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return food
            
                
    def search_food_by_name(self, search_food_name):
        for restaurant_account in self.__restaurant_account_list:
            for restaurant in restaurant_account.restaurant_list:
                for food in restaurant.food_list:
                    if food.name == search_food_name:
                        return food
                
    def search_restaurant_by_food_id(self, search_food_id):
        for restaurant in self.__restaurant_list:
            for food in restaurant.food_list:
                if food.id == search_food_id:
                    return food
                
    def search_restaurant_by_id(self, search_restaurant_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                if restaurant.restaurant_id == search_restaurant_id:
                    return restaurant

    def search_customer_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.current_order:
                if order.order_id == search_order_id:
                    return order
                
    def search_restaurant_order_by_id(self, search_order_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for order in restaurant.current_order_list:
                    if order.order_id == search_order_id:
                        return order
                
    def search_account_from_id(self, account_id: str):
        for customer in self.__customer_account_list:
            if customer.account_id == account_id:
                return customer
        for rider in self.__rider_account_list:
            if rider.account_id == account_id:
                return rider
        for restaurant in self.__restaurant_account_list:
            if restaurant.account_id == account_id:
                return restaurant
            
    def search_restaurant_by_order_id_and_account_id(self, order_id: str, account_id: str):
        account = self.search_account_from_id(account_id)
        if isinstance(account, RestaurantAccount):
            for restaurant in account.restaurant_list:
                for order in restaurant.get_order_list():
                    if order.order_id == order_id:
                        return restaurant
        return "Not found restaurant"

    def change_order_state(self, order: Order, order_state: str):
        order.order_state = order_state
        return "Order state changed"
            
    def get_account_order_state(self, account_id: str):
        account = self.search_account_from_id(account_id)
        order_dict = dict()
        if isinstance(account, RestaurantAccount):
            for restaurant in account.restaurant_list:
                for order in restaurant.get_order_list():
                    order_dict[order.order_id] = order.order_state
        else :
            for order in account.get_order_list():
                order_dict[order.order_id] = order.order_state
        return order_dict
            
    def get_account_payment_status(self, account_id: str):
        payment_dict = dict()
        account = self.search_account_from_id(account_id)
        if isinstance(account, RestaurantAccount):
            for restaurant in account.restaurant_list:
                for order in restaurant.get_order_list():
                    payment_dict[order.payment.transaction_id] = order.payment.payment_status
        else : 
            for order in account.get_order_list():
                payment_dict[order.payment.transaction_id] = order.payment.payment_status
        
        return payment_dict
            
    def customer_cancel_order(self, customer_account_id: str, order_id : str):
        customer_account = self.search_account_from_id(customer_account_id)
        order = self.search_customer_order_by_id(order_id)
        order_state = order.order_state
        if not isinstance(customer_account, CustomerAccount):
            return "Account is not customer account"
        if order_state == "Delivering":
            return "Cant cancel order, rider is delivering"
        else :
            if order_state == "Get_Rider":
                self.cancel_rider_order(order.rider, order)
            if order_state == "Get_Restaurant":
                for restaurant in order.restaurant_list:
                    self.cancel_restaurant_order(restaurant, order)
            order.change_payment_status("Refunded")
            customer_account.profile.top_up(order.payment.amount)
            self.change_order_state(order, "Cancelled by Customer")
            return customer_account_id + " " + order_id + " is cancelled. Payment is refunded."
        
    def restaurant_cancel_order(self, restaurant_account_id: str, order_id: str, food_name: str, string : str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        restaurant = self.search_restaurant_by_order_id_and_account_id(order_id, restaurant_account_id)
        order = self.search_restaurant_order_by_id(order_id)
        food = self.search_food_by_name(food_name)
        
        order_state = order.order_state
        if order_state == "Delivering":
            return "Cant cancel order, rider is delivering"
        order.remove_food_from_order(food)
        food_count = 0
        for food_in_restaurant in restaurant.food_list:
            for food_in_order in order.food_list:
                if food_in_restaurant == food_in_order:
                    food_count += 1
        if food_count == 0:
            order.remove_restaurant_from_order(restaurant)
            
        self.change_order_state(order,food_name + " Cancelled : " + string)
        order.rider.profile.pay_out(food.price)
        order.customer.profile.top_up(food.price)
        order.change_payment_status("Food : " + food_name + " is Refunded")
        return restaurant_account_id + " " + food.name + " in " + order_id + " is refund."

    def show_order_detail(self, order_id: str, account_id: str):
        if self.search_customer_order_by_id(order_id) != None:
            order = self.search_customer_order_by_id(order_id)
        elif self.seatch_restaurant_order_by_id(order_id) != None:
            order = self.seatch_restaurant_order_by_id(order_id)
        else :
            return "Order not found"
        order_detail = dict()
        order_detail["Order_ID"] = order.order_id
        order_detail["Customer"] = order.customer.account_id
        order_detail["Rider"] = order.rider.account_id
        restaurant_list = []
        for restaurant in order.restaurant_list:
            restaurant_list.append(restaurant.restaurant_name)
        order_detail["Restaurant"] = restaurant_list
        food_list = []
        for food in order.food_list:
            food_list.append(food.name)
        order_detail["Food"] = food_list
        order_detail["Order_State"] = order.order_state
        order_detail["Payment"] = order.payment.payment_status
        return order_detail
    
    def cancel_rider_order(self, rider_account: RiderAccount, order: Order):
        return "Order cancelled from rider"
    def cancel_restaurant_order(self, restaurant_account: RestaurantAccount, order: Order):
        order.rider.profile.pay_out(order.payment.amount)
        return "Order cancelled from restaurant"