from tkinter import *

win = Tk()
win.title("Worl's View")
win.config(bg = "lightblue")
win.geometry("450x450") # Set the window size to 500x500 pixels

name_label = Label(win, text="World's view Weather App",
                   font=("Time New Roman", 18, 'bold'))
name_label.place(x=20, y=40, height=45, width=400)



win.mainloop()