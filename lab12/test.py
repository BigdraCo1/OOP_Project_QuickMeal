import requests
import json
import base

respond1 = requests.post("http://127.0.0.1:8000/show/food_detail", json= {
        "account_id" : "101", "food_id" : "001"}).json()
print(respond1)

respond2 = requests.post("http://127.0.0.1:8000/show/food_detail", json= {
        "account_id" : "101", "food_id" : "002"}).json()
print(respond2)

respond3 = requests.post("http://127.0.0.1:8000/show/food_detail", json= {
        "account_id" : "101", "food_id" : "003"}).json()
print(respond3)

respond4 = requests.post("http://127.0.0.1:8000/show/food_detail", json= {
        "account_id" : "101", "food_id" : "004"}).json()
print(respond4)

payload = {"account_id" : "101"}
respond = requests.post("http://127.0.0.1:8000/cart", json = payload).json()
print(respond)

cart_text = ", ".join(respond)
print(cart_text)