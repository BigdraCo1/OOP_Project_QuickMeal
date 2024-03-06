import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import requests
import base
import json

API_ENDPOINT1 = "http://127.0.0.1:8000/show/restaurant"
API_ENDPOINT2 = "http://127.0.0.1:8000/show/menu"
API_ENDPOINT3= "http://127.0.0.1:8000/show/food_detail"
API_ENDPOINT4= "http://127.0.0.1:8000/cart"

def login(user_id, user_password):
    print("click")


def show_home():
    clear_menu()

    login_id = ttk.Entry(frame, bootstyle="SUCCESS")
    login_id.grid(row=1, column=1, padx=10, pady=5, sticky="news")

    login_pass = ttk.Entry(frame, bootstyle="SUCCESS")
    login_pass.grid(row=2, column=1, padx=10, pady=5, sticky="news")

    login_show_btn = ttk.Button(frame, text="Login", 
        command= login, bootstyle="SUCCESS")
    login_show_btn.grid(row=3, column=1, padx=10, pady=5)

def show_cart():
    pass

def show_restaurants():
    clear_menu()
    restaurants_list = requests.get(API_ENDPOINT1).json()
    print(restaurants_list)
    for i, restaurant in enumerate(restaurants_list, start=1):
        restaurant_btn = ttk.Button(frame, text=f"{restaurant}",
                                 command=lambda r=restaurant: show_menu(r))
        restaurant_btn.grid(row=i, column=1, padx=10, pady=5, sticky="news", columnspan=2)

    go_back_btn = ttk.Button(frame, text="Go Back", command=show_home, bootstyle="SUCCESS")
    go_back_btn.grid(row=len(restaurants_list)+1, column=2, padx=10, pady=5, sticky="news")

def show_menu(restaurant):
    clear_menu()
    payload = base.restaurant_name(restaurant_name = str(restaurant))
    food_list = requests.post(API_ENDPOINT2, payload.json()).json()

    print(food_list)
    for i, food in enumerate(food_list, start=1):
        food_btn = ttk.Button(frame, text=f"{food}",
                                 command=lambda f = food, r=restaurant: show_food_detail(f, r))
        food_btn.grid(row=i, column=0, padx=10, pady=5, columnspan=2, sticky="news")

    go_back_btn = ttk.Button(frame, text="Go Back", command=show_restaurants, bootstyle="SUCCESS")
    go_back_btn.grid(row=len(food_list)+1, column=1, padx=10, pady=5, sticky="news")

def show_food_detail(food, restaurant):
    clear_menu()
    payload = {
        "restaurant_name" : restaurant,
        "food_name" : food
    }
    food_detail = requests.get(API_ENDPOINT3, json = payload).json()
    name_label = ttk.Label(frame, text=f'{food_detail["food_name"]} detail :')
    name_label.grid(row=0, column=1, padx=10, pady=5, sticky="news")
    restaurant_label = ttk.Label(frame, text=food_detail["restaurant_name"])
    restaurant_label.grid(row=1, column=1, padx=10, pady=5, sticky="news")
    price_label = ttk.Label(frame, text=food_detail["food_price"])
    price_label.grid(row=2, column=1, padx=10, pady=5, sticky="news")

    add_btn = ttk.Button(frame, text="Add", command=lambda f=food_detail["food_id"]: add_to_cart(str(temp_entry.get()), f), bootstyle="SUCCESS")
    add_btn.grid(row=3, column=0, padx=10, pady=5, sticky="news")

    temp_entry = ttk.Entry(frame, bootstyle="SUCCESS")
    temp_entry.grid(row=3, column=1, padx=10, pady=5, sticky="news")

    go_back_btn = ttk.Button(frame, text="Go Back", command=lambda r=restaurant: show_menu(r), bootstyle="SUCCESS")
    go_back_btn.grid(row=3, column=2, padx=10, pady=5, sticky="news")

def add_to_cart(acc_id, food_id):   
    payload = {
        "account_id" : acc_id,
        "food_id" : food_id
    }
    respond = requests.post(API_ENDPOINT3, json= payload).json()
    print(respond)
    if respond == "fail to add food to your card":
        error_message = Messagebox.show_error(respond, "Your Cart")
    else:    
        add_message = Messagebox.show_info(respond, "Your Cart")
        check(acc_id)

def check(id):
    payload = {"account_id" : id}
    cart_list = requests.post(API_ENDPOINT4, json = payload).json()

    if type(cart_list)!= list: 
        error_text = ttk.Label(frame, text= "Customer Not Found")
        error_text.grid(row = 5, colum = 1, padx = 10, pady = 5, sticky="news")
    print(cart_list)
    for i, food in enumerate(cart_list, start=0):
        food_label = ttk.Label(frame, text=food)
        food_label.grid(row= 5+(i//3), column= i%3, padx=10, pady=5, sticky="news")

def clear_menu():
    # Clear previous menu items
    for widget in frame.winfo_children():
        widget.destroy()

root = ttk.Window(themename='journal')
root.title("QuickMeal") 
root.geometry("500x500")

title_label = ttk.Label(root, text="QuickMeal", bootstyle="PRIMARY", font=('TkDefaultFont', 20))
title_label.pack(pady=20, anchor='center')

frame = ttk.Frame(root)
frame.pack(padx=10, expand=False)


show_home()

root.mainloop()