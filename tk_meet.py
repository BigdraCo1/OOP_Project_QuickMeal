# import tkinter as tk
from tkinter import *
import requests

API_ENDPOINT1 = "http://127.0.0.1:8000/get_available_room"
API_ENDPOINT2 = "http://127.0.0.1:8000/book_room"

def on_click2():
    user_list = user1.get().split()
    print(user_list)
    payload = {
        "subject" : subject.get(),
        "room_id" :  select_opt.get(),
        "user" : user_list,
        "start_date": st_date.get(),
        "start_time": st_time.get(),
        "end_date": end_date.get(),
        "end_time": end_time.get()
    }
    response = requests.post(API_ENDPOINT2, json=payload)
    if response.ok:
        Label(root, text="This booking :"+ str(response.json())).grid(row=20, column=1, padx = 5, pady=5)
        

def on_click():
    print("on click")
    payload = {
        "start_date": st_date.get(),
        "start_time": st_time.get(),
        "end_date": end_date.get(),
        "end_time": end_time.get(),
        "capacity": capacity.get()
    }
    response = requests.post(API_ENDPOINT1, json=payload)
    if response.ok:
        data = response.json()
        data = data['Data']
        print(data)
        i=0
        menu = om["menu"]
        menu.delete(0, "end")
        for key, value in data.items():
            temp = key #+ ":"+ str(value)
            menu.add_command(label=temp,command=lambda value=temp: select_opt.set(value))
    return

def set_input1():
    st_date.set("26-03-2023")
    st_time.set("09:00")
    end_date.set("26-03-2023")
    end_time.set("16:00")
    capacity.set("30")


root = Tk()
root.option_add("*Font", "impact 18")
st_date = StringVar()
st_time = StringVar()
end_date = StringVar()
end_time = StringVar()
capacity = StringVar()
select_opt = StringVar()

user1 = StringVar()
subject = StringVar()
data_list = ['0']

Label(root, text="Start Date :").grid(row=0, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=st_date, width=12, justify="left").grid(row=0, column=1, padx=10)
Label(root, text="Start Time :").grid(row=1, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=st_time, width=12, justify="left").grid(row=1, column=1, padx=10)
Label(root, text="End Date :").grid(row=2, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=end_date, width=12, justify="left").grid(row=2, column=1, padx=10)
Label(root, text="End Time :").grid(row=3, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=end_time, width=12, justify="left").grid(row=3, column=1, padx=10)
Label(root, text="Capacity :").grid(row=4, column=0,padx=10, ipady=5, sticky='E')
Entry(root, textvariable=capacity, width=12, justify="left").grid(row=4, column=1, padx=10)
set_input1()
Button(root, text=" Search ", bg="green", command=on_click).grid(row=5, column=0, columnspan=2)

om = OptionMenu(root, select_opt, *data_list)
om.grid(row=6, column=1)
om.config(width=15)
Label(root, text="User :").grid(row=7, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=user1, width=12, justify="left").grid(row=7, column=1, padx=10)
Label(root, text="Subject :").grid(row=8, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=subject, width=12, justify="left").grid(row=8, column=1, padx=10)
Button(root, text=" Book ", bg="green", command=on_click2).grid(row=9, column=0, columnspan=2)

root.mainloop()
