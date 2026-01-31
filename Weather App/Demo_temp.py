from tkinter import *
from tkinter import ttk
import requests

win = Tk()
win.title("Worl's View")
win.config(bg = "lightblue")
win.geometry("450x480") # Set the window size to 450x480 pixels

name_label = Label(win, text="World's view Weather App",
                   font=("Time New Roman", 18, 'bold'))
name_label.place(x=20, y=45, height=45, width=400)

# Create combobox for city selection
list_name = [
    "Dhaka",
    "Chattogram",
    "Khulna",
    "Rajshahi",
    "Sylhet",
    "Rangpur",
    "Mymensingh",
    "Barisal",
    "Narayanganj",
    "Gazipur",
    "Comilla",
    "Dinajpur",
    "Jessore",
    "Bogra"
]
com = ttk.Combobox(win, text="World's view Weather App", values= list_name,
                   font=("Time New Roman", 14, 'bold'))
com.place(x=20, y=110, height=40, width=400)

#Create button to get weather
done_button = Button(win, text="Done",
                   font=("Time New Roman", 14, 'bold'))
done_button.place(y=165, height=35, width=85, x=170)


w_label = Label(win, text="Weather Climate",
                   font=("Time New Roman", 14))
w_label.place(x=20, y=220, height=45, width=170)
w_label1 = Label(win, text="",
                   font=("Time New Roman", 14))
w_label1.place(x=200, y=220, height=45, width=170)


wb_label = Label(win, text="Weather Description",
                   font=("Time New Roman", 13))
wb_label.place(x=20, y=280, height=45, width=170)
wb_label1 = Label(win, text="",
                   font=("Time New Roman", 13))
wb_label1.place(x=200, y=280, height=45, width=170)


temp_label = Label(win, text="Temperature",
                   font=("Time New Roman", 13))
temp_label.place(x=20, y=340, height=45, width=170)
temp_label1 = Label(win, text="",
                   font=("Time New Roman", 13))
temp_label1.place(x=200, y=340, height=45, width=170)


per_label = Label(win, text="Pressure",
                   font=("Time New Roman", 13))
per_label.place(x=20, y=400, height=45, width=170)
per_label1 = Label(win, text="",
                   font=("Time New Roman", 13))
per_label1.place(x=200, y=400, height=45, width=170)



win.mainloop()