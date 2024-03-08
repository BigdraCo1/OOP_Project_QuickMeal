from datetime import datetime
from internals.payment import Payment

from internals.custom_account import CustomerAccount
from internals.rider_account import RiderAccount
from internals.restaurant_account import RestaurantAccount
from internals.restaurant import Restaurant
from internals.review import Review
from internals.order import Order



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
    def restaurant_account_list(self):
        return self.__restaurant_account_list

    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant_account(self, new_restaurant: RestaurantAccount):
        self.__restaurant_account_list.append(new_restaurant)

    def remove_customer_account(self, customer_account: CustomerAccount):
        self.__customer_account_list.remove(customer_account)
        del customer_account
        
    def remove_rider_account(self, rider_account: RiderAccount):
        self.__rider_account_list.remove(rider_account)
        del rider_account
        
    def remove_restaurant_account(self, restaurant_account: RestaurantAccount):
        self.__restaurant_account_list.remove(restaurant_account)
        del restaurant_account

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

    def edit_menu(self, restaurant, menu, request):
        acc_restaurant = self.search_restaurant(restaurant)
        if isinstance(acc_restaurant, str):
            return acc_restaurant
        return acc_restaurant.edit_menu(menu, request)
    
    def confirm_customer_order(self, customer_id, order_id):
        #search customer from customer_list 
        customer = self.search_customer_by_id(customer_id)
        if customer == None:
            return f"customer_id : {customer_id} not found"
        #search order from order_list
        order = customer.search_order_by_id(order_id)
        if order == None:
            return f"order_id : {order_id} not found"
        # calculate amount
        amount = sum(food.price for food in order.food_list)
        if customer.pocket.balance < amount:
            return "Insufficient balance"
        # pay out
        customer.pocket.pay_out(amount)
        # create payment object
        payment_time = datetime.now()
        food_list = []
        for food in order.food_list:
            food_list.append(food)
        payment = Payment(food_list,amount,"paid",order.restaurant_list,payment_time.strftime("%c"),order_id)
        order.order_state = "confirmed"
        order.payment = payment
        # return f"order_id : {order.order_id} confirmed, amount : {amount}"
        return [{"order_id": order.order_id, "order_state": order.order_state, "amount": amount}]

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
                
    def search_order_by_id(self, search_order_id):
        for customer in self.__customer_account_list:
            for order in customer.order_list:
                if order.order_id == search_order_id:
                    return order
                
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
                food_dict[food.id] = [ food.name, food.price ]
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
        if basket != [] :
            basket_dict["total"] = self.calculate_total_of_basket(customer_id)
            basket_dict["address"] = basket[0].customer_address
            for order in basket:
                already_add = []
                for food in order.food_list:
                    if food not in already_add:
                        quantity = len([f for f in order.food_list if (f.id == food.id and f.current_size == food.current_size)])
                        basket_dict[f"id-{food.id} {food.current_size}"] = [quantity, food.id, 
                            food.name, food.price + food.size[str(food.current_size)], food.current_size]
                        already_add.append(food)
        return basket_dict 
    
    def show_address(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        return [address for address in customer.address_list]

    def add_address_to_basket(self, customer_id, address):
        customer = self.search_customer_by_id(customer_id)
        basket = customer.current_order
        for order in basket:
            order.customer_address = address
        return f"{address} is now set as address of your order"
    
    def show_food_detail(self, food_id):
        food = self.search_food_by_id(food_id)
        return {"food_id"    : food.id,
                "food_name"  : food.name,
                "food_type"  : food.type,
                "food_size"  : food.size,
                "food_price" : food.price}
    
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
        else :
            for order in customer.current_order:
                if order.restaurant == restaurant :
                    if order.food_list != [] :
                        return f"{size} {food.name} is remove from basket"
                    customer.current_order.remove(order)
                    return f"{size} {food.name} is remove from basket"
        
    #ถ้ามาพร้อม change_quantity ให้ change_quantity ก่อน
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
        if restaurant.reviewed_list == [] : return {}
        else:
            dct = {}
            num = 1
            for review in restaurant.reviewed_list:
                dct[f"{num}"] =  [review.rate, review.comment]
                num += 1
        return dct
    
    def add_review_to_restaurant(self, customer_id, rating, comment, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        review = Review(rating, comment, customer, "TYPE")
        customer.reviewed_list.append(review)
        restaurant.reviewed_list.append(review)
        return f"you have writing a review to {restaurant.name_restaurant}"
    
    def remove_review_from_restaurant(self, customer_id, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for review in restaurant.reviewed_list:
            if review.customer == customer:
                restaurant.reviewed_list.remove(review)
                customer.reviewed_list.remove(review)
                del review
        return f"you have remove a review from {restaurant.name_restaurant}"
    
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
            for order in rider.recieve_order_list:
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
        for restaurant in self.__restaurant_account_list:
            if restaurant.account_id == account_id:
                return restaurant
            
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
        restaurant = self.search_restaurant_by_order_id(order_id)
        if not order in restaurant.requested_order_list:
            return "Order not in requested_order_list."
        order_state = order.order_state
        if self.check_order_state(order_state) != None :
            return self.check_order_state(order_state)
        order.change_payment_status("Refunded")
        customer_account.pocket.top_up(order.payment.amount)
        self.change_order_state(order, "Cancelled by Customer")
        customer_account.pocket.add_payment(order.payment)
        order.rider.add_finished_order(order)
        order.rider.remove_recieved_order(order)
        order.restaurant.add_finished_order(order)
        order.restaurant.remove_requested_order(order)
        return customer_account_id + " Order ID : " + order_id + " is cancelled. Payment is refunded."
     
    def rider_cancel_order(self, rider_account_id: str, order_id: str):
        rider_account = self.search_account_from_id(rider_account_id)
        if not isinstance(rider_account, RiderAccount):
            return "Account is not rider account"
        order = self.search_rider_order_by_id(order_id)
        restaurant = self.search_restaurant_by_order_id(order_id)
        if not order in restaurant.requested_order_list:
            return "Order not in requested_order_list."
        order_state = order.order_state
        if self.check_order_state(order_state) != None :
            return self.check_order_state(order_state)
        order.change_payment_status("Refunded")
        order.customer.pocket.top_up(order.payment.amount)
        self.change_order_state(order, "Cancelled by Rider")
        rider_account.pocket.add_payment(order.payment)
        order.rider.add_finished_order(order)
        order.rider.remove_recieved_order(order)
        order.restaurant.add_finished_order(order)
        order.restaurant.remove_requested_order(order)
        return rider_account_id + " Order ID : " + order_id + " is cancelled."
    
    def restaurant_cancel_order(self, restaurant_account_id: str, order_id: str, food_name: str, string : str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        if not isinstance(restaurant_account, RestaurantAccount):
            return "Account is not restaurant account"
        restaurant = self.search_restaurant_by_order_id(order_id)
        if self.search_restaurant_order_by_id(order_id) == None:
            return "Order not found"
        order = self.search_restaurant_order_by_id(order_id)
        if not order in restaurant.requested_order_list:
            return "Order not in requested_order_list."
        if self.search_food_by_name(food_name) == None:
            return "Food not found."
        food = self.search_food_by_name(food_name)
        if food not in restaurant.food_list:
            return "Food not found in restaurant."
        if food not in order.food_list:
            return "Food not found in order."
        order_state = order.order_state
        if self.check_order_state(order_state) != None :
            return self.check_order_state(order_state)
        if food_name in order_state:
            return "Food already cancelled."
        order.remove_food_from_order(food)
        self.change_order_state(order,order_state + "\n" + food_name + " Cancelled : " + string)
        if order.food_list == []:
            self.change_order_state(order, "Cancelled by Restaurant.")
            
        order.rider.pocket.pay_out(food.price)
        order.customer.pocket.top_up(food.price)
        order.change_payment_status(order.payment.payment_status +" Food : " + food_name + " is Refunded")
        if order.food_list == []:
            order.rider.add_finished_order(order)
            order.rider.remove_recieved_order(order)
            order.restaurant.add_finished_order(order)
            order.restaurant.remove_requested_order(order)
            order.change_payment_status("Refunded")
            return restaurant_account_id + " Order ID : " + order_id + " is cancelled."
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
        order_detail["Restaurant"] = order.restaurant.name_restaurant
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
    
    def check_order_state(self, order_state : str):
        if order_state == "Delivering":
            return "Cant cancel order, rider is delivering"
        if order_state == "Cancelled by Customer":
            return "Order already cancelled by customer"
        if order_state == "Cancelled by Rider":
            return "Order already cancelled by rider"
        if order_state == "Cancelled by Restaurant":
            return "Order already cancelled by restaurant"
            
        return None
    
    def show_request_order_list_in_restaurant(self, restaurant_account_id: str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        if not isinstance(restaurant_account, RestaurantAccount):
            return "Account is not restaurant account"
        request_order_dict = dict()
        order_detail_list = list()
        for restaurant in restaurant_account.restaurant_list:
            for request_order in restaurant.request_order_list:
                order_detail_list.append(self.show_order_detail(request_order.order_id))
        request_order_dict[restaurant.name_restaurant] = order_detail_list
        return request_order_dict
    
    def show_requested_order_list_in_restaurant(self, restaurant_account_id: str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        if not isinstance(restaurant_account, RestaurantAccount):
            return "Account is not restaurant account"
        requested_order_dict = dict()
        order_detail_list = list()
        for restaurant in restaurant_account.restaurant_list:
            for requested_order in restaurant.requested_order_list:
                order_detail_list.append(self.show_order_detail(requested_order.order_id))
        requested_order_dict[restaurant.name_restaurant] = order_detail_list
        return requested_order_dict
    
    def show_finish_order_list_in_restaurant(self, restaurant_account_id: str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        if not isinstance(restaurant_account, RestaurantAccount):
            return "Account is not restaurant account"
        finish_order_dict = dict()
        order_detail_list = list()
        for restaurant in restaurant_account.restaurant_list:
            for finished_order in restaurant.finished_order_list:
                order_detail_list.append(self.show_order_detail(finished_order.order_id))
        finish_order_dict[restaurant.name_restaurant] = order_detail_list
        return finish_order_dict
    
    def restaurant_receive_order_from_customer(self, restaurant_account_id:str, order_id:str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        restaurant = self.search_restaurant_by_order_id(order_id)
        restaurant.receive_order_from_customer(order_id)
        order = self.search_restaurant_order_by_id(order_id)
        for rider in self.rider_account_list:
            rider.add_request_order(order)
        return f"{restaurant_account_id} Order : {order_id} is recieve."

    def restaurant_deny_receive_order_from_customer(self, restaurant_account_id:str, order_id:str):
        restaurant_account = self.search_account_from_id(restaurant_account_id)
        restaurant = self.search_restaurant_by_order_id(order_id)
        order = self.search_restaurant_order_by_id(order_id)
        order.state = "Deny by restaurant."
        order.payment.payment_status = "Refunded"
        restaurant.remove_request_order(order)
        return f"{restaurant_account_id} Order : {order_id} is deny."