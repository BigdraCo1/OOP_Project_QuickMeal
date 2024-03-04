import ttkbootstrap as ttk

restaurants_list = [
    {"name": "Restaurant A", "rating": 4.5, "cuisine": "Italian", "menu": ["Pizza", "Pasta", "Salad"]},
    {"name": "Restaurant B", "rating": 4.2, "cuisine": "Mexican", "menu": ["Tacos", "Burritos", "Quesadillas"]},
    {"name": "Restaurant C", "rating": 4.8, "cuisine": "Chinese", "menu": ["Kung Pao Chicken", "Fried Rice", "Spring Rolls"]},
    {"name": "Restaurant D", "rating": 4.0, "cuisine": "Indian", "menu": ["Curry", "Naan", "Samosa"]},
]

def show_home():
    clear_menu()
    show_btn = ttk.Button(frame, text="Show Available Restaurants", command=show_restaurants)
    show_btn.grid(row=0, column=0, padx=10, pady=5)

def show_restaurants():
    clear_menu()
    for i, restaurant in enumerate(restaurants_list, start=1):
        restaurant_btn = ttk.Button(frame, text=f"{restaurant['name']} - Rating: {restaurant['rating']} - Cuisine: {restaurant['cuisine']}",
                                 command=lambda r=restaurant['name']: show_menu(r))
        restaurant_btn.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    go_back_btn = ttk.Button(frame, text="Go Back", command=show_home)
    go_back_btn.grid(row=len(restaurants_list)+1, column=0, padx=10, pady=5, sticky="w")

def show_menu(restaurant):
    clear_menu()
    restaurant_data = next((r for r in restaurants_list if r["name"] == restaurant), None)
    if restaurant_data:
        # Clear previous menu
        clear_menu()
        # Display menu items
        for i, item in enumerate(restaurant_data["menu"], start=1):
            label = ttk.Label(frame, text=f"{i}. {item}")
            label.grid(row=i, column=1, padx=10, pady=5, sticky="w")

        go_back_btn = ttk.Button(frame, text="Go Back", command=show_restaurants)
        go_back_btn.grid(row=len(restaurant_data["menu"])+1, column=0, padx=10, pady=5, sticky="w")

def clear_menu():
    # Clear previous menu items
    for widget in frame.winfo_children():
        widget.destroy()

root = ttk.Window(themename='journal')
root.title("QuickMeal") 
root.geometry("500x500")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, expand=True)

show_home()

root.mainloop()