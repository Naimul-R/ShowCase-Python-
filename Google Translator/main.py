from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg='skyblue')


lab_txt = Label(root, text='Translator', font=('Time New Roman', 25, 'bold'), bg='lightblue')
lab_txt.place(x=110, y=40, height=50, width=260)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text='Source Text', font=('Time New Roman', 15, 'bold'), fg='Black', bg='skyblue')
lab_txt.place(x=110, y=100, height=20, width=260)

src_txt = Text(frame, font=('Time New Roman', 15, 'bold'), wrap=WORD)
src_txt.place(x=10, y=130, height=150, width=480)


root.mainloop()