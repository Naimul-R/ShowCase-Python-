import tkinter as tk

calculation = ""

def add_to_calculation(sysmbol):
    pass


def evaluate_calculation():
    pass


def clear_calculation():
    pass


root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
root.mainloop()