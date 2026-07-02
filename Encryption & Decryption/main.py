from tkinter import *
from tkinter import messagebox
import base64
import os 

def main_screen():
    screen=Tk()
    screen.geometry("375x398")
    
    #Icon
    image_icon = PhotoImage(file='keys.png')
    screen.iconphoto(False,image_icon)
    screen.title("PctApp")
    
    Label(text="Enter the text for Encryption & Decryption", fg="black", font=("calbri", 13)).place(x=10,y=10)
    text1 = Text(font="Robote 16",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    
    screen.mainloop()
    
main_screen()