from internals.rider_account import RiderAccount
from internals.restaurant_account import RestaurantAccount
from internals.custom_account import CustomerAccount
from internals.restaurant import Restaurant
from internals.order import Order
from internals.food import Food


class Controller:
    def __init__(self, customer_account_list: list[CustomerAccount], rider_account_list: list[RiderAccount],
                 restaurant_list: list[RestaurantAccount]):
        self.__customer_account_list = customer_account_list
        self.__rider_account_list = rider_account_list
        self.__restaurant_account_list = restaurant_list
        self.__approval_list = None

    @property
    def customer_account_list(self):
        return self.__customer_account_list

    @property
    def rider_account_list(self):
        return self.__rider_account_list

    @property
    def restaurant_account_list(self):
        return self.__restaurant_account_list

    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant(self, new_restaurant: RestaurantAccount):
        self.__restaurant_account_list.append(new_restaurant)

    def remove_customer_account(self, customer: CustomerAccount):
        self.__customer_account_list.remove(customer)
        del customer

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
        return 'Not found restaurantssssssssssssssssssssssssssssssss'

    def get_menu_list(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, str):
            return restaurant
        return restaurant.food_list

    def search_menu_and_restaurant(self, key: str):
        show_list = []
        restaurant_list = self.restaurant_account_list
        for restaurant_acc in restaurant_list:
            for restaurant in restaurant_acc.restaurant_list:
                name = restaurant.name_restaurant
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

    def new_menu(self, restaurant, request):
        real_restaurant = self.search_restaurant(restaurant)
        return real_restaurant.add_menu(request)

    def search_current_order_by_id(self, search_order_id):
        for customer in self.customer_account_list:
            if customer.current_order.order_id == search_order_id:
                return customer.current_order

        
    def search_customer_by_id(self, search_account_id):
        for customer in self.customer_account_list:
            if customer.account_id == search_account_id:
                return customer
            
    def search_food_by_id(self, search_food_id):
        for restaurant_acc in self.restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                for food in restaurant.food_list:
                    if food.id == search_food_id:
                        return food
                    
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
                        return food
                
    def search_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.order_list:
                if order.order_id == search_order_id:
                    return order
                
    def search_rider_order_by_id(self, search_order_id):
        for rider in self.__rider_account_list:
            for order in rider.recieve_order_list:
                if order.order_id == search_order_id:
                    return order
                
    def search_restaurant_order_by_id(self, search_order_id):
        for restaurant_acc in self.__restaurant_account_list:
            for restaurant in restaurant_acc.restaurant_list:
                if restaurant.requested_order_list != None:
                    for order in restaurant.requested_order_list:
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
                for order in restaurant.requested_order_list:
                    if order.order_id == order_id:
                        return restaurant
        return "Not found restaurantsssssxcxcxcxcxcx"

    def change_order_state(self, order: Order, order_state: str):
        order.order_state = order_state
        return "Order state changed"
            
    def customer_cancel_order(self, customer_account_id: str, order_id : str):
        customer_account = self.search_account_from_id(customer_account_id)
        if not isinstance(customer_account, CustomerAccount):
            return "Account is not customer account"
        if self.search_customer_order_list_by_id(order_id) == None:
            return "Order not found"
        order = self.search_customer_order_list_by_id(order_id)
        order_state = order.order_state
        if order_state == "Delivering":
            return "Cant cancel order, rider is delivering"
        if order_state == "Cancelled by Customer":
            return "Order already cancelled"
        if order_state == "Get_Restaurant":
            order.rider.pocket.pay_out(order.payment.amount)
        order.change_payment_status("Refunded")
        customer_account.pocket.top_up(order.payment.amount)
        self.change_order_state(order, "Cancelled by Customer")
        customer_account.pocket.add_payment(order.payment)
        return customer_account_id + " " + order_id + " is cancelled. Payment is refunded."
    
    def rider_cancel_order(self, rider_account_id: str, order_id: str):
        rider_account = self.search_account_from_id(rider_account_id)
        if not isinstance(rider_account, RiderAccount):
            return "Account is not rider account"
        order = self.search_rider_order_by_id(order_id)
        order_state = order.order_state
        if order_state == "Delivering":
            return "Cant cancel order, rider is delivering"
        if order_state == "Cancelled by Customer":
            return "Order already cancelled"
        if order_state == "Cancelled by Rider":
            return "Order already cancelled"
        if order_state == "Get_Restaurant":
            order.rider.pocket.pay_out(order.payment.amount)
        order.change_payment_status("Refunded")
        order.customer.pocket.top_up(order.payment.amount)
        self.change_order_state(order, "Cancelled by Rider")
        rider_account.pocket.add_payment(order.payment)
        return rider_account_id + " " + order_id + " is cancelled."
    
    def restaurant_cancel_order(self, restaurant_account_id: str, order_id: str, food_name: str, string : str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        if not isinstance(restaurant_account, RestaurantAccount):
            return "Account is not restaurant account"
        restaurant = self.search_restaurant_by_order_id_and_account_id(order_id, restaurant_account_id)
        if self.search_restaurant_order_by_id(order_id) == None:
            return "Order not found"
        order = self.search_restaurant_order_by_id(order_id)
        if self.search_food_by_name(food_name) == None:
            return "Food not found"
        food = self.search_food_by_name(food_name)
        if food not in restaurant.food_list:
            return "Food not found in restaurant"
        order_state = order.order_state
        if order_state == "Delivering":
            return "Cant cancel order, rider is delivering"
        if order_state == "Cancelled by Customer":
            return "Order already cancelled"
        if order_state == "Cancelled by Rider":
            return "Order already cancelled"
        if food_name in order_state:
            return "Food already cancelled"
        order.remove_food_from_order(food)
        food_count = 0
        for food_in_restaurant in restaurant.food_list:
            for food_in_order in order.food_list:
                if food_in_restaurant == food_in_order:
                    food_count += 1
        if food_count == 0:
            order.remove_restaurant_from_order(restaurant)
            
        self.change_order_state(order,order_state + "\n" + food_name + " Cancelled : " + string)
        order.rider.pocket.pay_out(food.price)
        order.customer.pocket.top_up(food.price)
        order.change_payment_status(order.payment.payment_status +"Food : " + food_name + " is Refunded")
        return restaurant_account_id + " " + food.name + " in " + order_id + " is refund."
    
        

    def show_order_detail(self, order_id: str):
        order_detail = dict()
        if self.search_customer_order_list_by_id(order_id) != None:
            order = self.search_customer_order_list_by_id(order_id)
        else :
            order_detail["Order_Not_Found"] = order_id + " is not found in list"
            return order_detail

        if not isinstance(order, Order):
            return order
            
        
        order_detail["Order_ID"] = order.order_id
        order_detail["Customer"] = order.customer.account_id
        order_detail["Rider"] = order.rider.account_id
        restaurant_list = []
        for restaurant in order.restaurant_list:
            restaurant_list.append(restaurant.name_restaurant)
        order_detail["Restaurant"] = restaurant_list
        food_list = []
        for food in order.food_list:
            food_list.append(food.name)
        order_detail["Food"] = food_list
        order_detail["Order_State"] = order.order_state
        order_detail["Payment"] = order.payment.payment_status
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
            for restaurant in account.restaurant_list:
                for order in restaurant.requested_order_list:
                    payment_dict[order.payment.transaction_id] = [order.payment.payment_status, order.payment.amount]
        elif isinstance(account, CustomerAccount):
            for order in account.order_list:
                payment_dict[order.payment.transaction_id] = [order.payment.payment_status, order.payment.amount]
        elif isinstance(account, RiderAccount):
            for order in account.recieve_order_list:
                payment_dict[order.payment.transaction_id] = [order.payment.payment_status, order.payment.amount]
                
        return payment_dict