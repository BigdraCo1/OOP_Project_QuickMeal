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
                restaurant_account_list: list[RestaurantAccount], order_list: list[Order]):
        self.__customer_account_list = customer_account_list
        self.__rider_account_list = rider_account_list
        self.__restaurant_account_list = restaurant_account_list
        self.__order_list = []
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
    
    @property
    def order_list(self):
        return self.__order_list
    
    # {method} add function

    def add_customer_account(self, new_customer: CustomerAccount):
        self.__customer_account_list.append(new_customer)

    def add_rider_account(self, new_rider: RiderAccount):
        self.__rider_account_list.append(new_rider)

    def add_restaurant_account(self, new_restaurant: RestaurantAccount):
        self.__restaurant_account_list.append(new_restaurant)
        
    def add_order(self, new_order: Order):
        self.__order_list.append(new_order)
        
    # [method] remove function

    def remove_customer_account(self, customer_account: CustomerAccount):
        self.__customer_account_list.remove(customer_account)
        del customer_account
        
    def remove_rider_account(self, rider_account: RiderAccount):
        self.__rider_account_list.remove(rider_account)
        del rider_account
        
    def remove_restaurant_account(self, restaurant_account: RestaurantAccount):
        self.__restaurant_account_list.remove(restaurant_account)
        del restaurant_account
        
    def remove_order(self, order: Order):
        self.__order_list.remove(order)
        del order

    def remove_restaurant(self, restaurant_name: str):
        restaurant = self.search_restaurant(restaurant_name)
        if isinstance(restaurant, Restaurant):
            restaurant_acc = restaurant.owner
            restaurant_acc.remove_restaurant(restaurant)
            del restaurant
            return 'Success'
        return 'Not Found'
    
    # [method] search function
    
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
        return "Not found restaurants"

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
    
    # [method] customer function
    
    def show_basket(self, customer_id):
        customer = self.search_customer_by_id(customer_id)
        order = customer.current_order
        order_dict = {}
        already_add = []
        if order != None :
            for food in order.food_list:
                if food not in already_add:
                    amount = len([f for f in order.food_list if (f.id == food.id and f.current_size == food.current_size)])
                    order_dict[f"id-{food.id} {food.current_size}"] = [amount, food.id, 
                        food.name, food.price + food.size[str(food.current_size)], food.current_size]
                    already_add.append(food)
        return order_dict
    
    def add_food_to_basket(self, customer_id, food_id, size, amount):
        customer = self.search_customer_by_id(customer_id)
        food = self.search_food_by_id(food_id)
        restaurant = self.search_restaurant_by_food_id(food_id)
        customer.add_food(food, size, amount)
        if restaurant not in customer.current_order.restaurant_list:
            customer.current_order.restaurant_list.append(restaurant)
        return str(amount) + " x " + str(food.name) + " is added to your cart!"
    
    def add_address_to_basket(self, customer_id, address):
        customer = self.search_customer_by_id(customer_id)
        order = customer.current_order
        order.customer_address = address
        return "the address of your order has been set!"
    
    def change_size(self, customer_id, food_id, size, new_size):
        customer = self.search_customer_by_id(customer_id)
        order = customer.current_order
        food = self.search_food_by_id(food_id)
        for customer_food in order.food_list:
            if customer_food.id == food.id and customer_food.current_size == size:
                customer_food.current_size = new_size
        return str(food.name) + " is now" + str(new_size)
    
    def change_amount(self, customer_id, food_id, amount, new_amount, size):
        customer = self.search_customer_by_id(customer_id)
        food = self.search_food_by_id(food_id)
        restaurant = self.search_restaurant_by_food_id(food_id)
        customer.remove_food(food_id, size, amount)
        if new_amount > 0:
            customer.add_food(food, size, new_amount)
            return str(food.name) + " is now" + str(new_amount)
        else :
            for f in customer.current_order.food_list:
                if self.search_restaurant_by_food_id(f.id) == restaurant:
                    return str(food.name) + " is remove from basket"
            customer.current_order.restaurant_list.remove(restaurant)
            return str(food.name) + " is remove from basket"
    
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
    
    def add_review_to_restaurant(self, customer_id, rating, comment, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        review = Review(rating, comment, customer, "TYPE")
        customer.reviewed_list.append(review)
        restaurant.reviewed_list.append(review)
        return "you have writing a review to " + str(restaurant.name_restaurant)
    
    # [method] rider function 
    
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
    
    # [method] restaurant function
    
    def show_restaurant(self):
        restaurant_dict = {}
        for restaurant_account in self.__restaurant_account_list:
            for restaurant in restaurant_account.restaurant_list:
                restaurant_dict[restaurant.restaurant_id] = [
                    restaurant.name_restaurant, restaurant.restaurant_location, restaurant.rate ]
        return restaurant_dict
    
    def show_restaurant_menu(self, restaurant_id):
        food_dict = {}
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for food in restaurant.food_list:
                food_dict[food.id] = [ food.name, food.price ]
        return food_dict
    
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

    def remove_menu(self, restaurant, menu):
        real_restaurant = self.search_restaurant(restaurant)
        if isinstance(real_restaurant, str):
            return real_restaurant
        return real_restaurant.remove_food(menu)

    def new_menu(self, restaurant, request):
        real_restaurant = self.search_restaurant(restaurant)
        return real_restaurant.add_menu(request)
    
    def show_food_detail(self, food_id):
        food = self.search_food_by_id(food_id)
        return {"food_id"    : food.id,
                "food_name"  : food.name,
                "food_type"  : food.type,
                "food_size"  : food.size,
                "food_price" : food.price}
    
    def show_review(self, restaurant_id):
        restaurant = self.search_restaurant_by_id(restaurant_id)
        if restaurant.review_list == [] :
            return {}
        else:
            dct = {}
            for review in restaurant.review_list:
                dct[review.customer.profile.fullname] =  [review.rate, review.comment]
        return dct
    
    def remove_review_from_restaurant(self, customer_id, restaurant_id):
        customer = self.search_customer_by_id(customer_id)
        restaurant = self.search_restaurant_by_id(restaurant_id)
        for review in restaurant.review_list:
            if review.customer == customer:
                restaurant.review_list.remove(review)
                customer.review_list.remove(review)
                del review
        return "you have remove a review from " + str(restaurant.name)
    
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
    
    # [method] order function

    def change_order_state(self, order: Order, order_state: str):
        order.order_state = order_state
        return "Order state changed"

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
