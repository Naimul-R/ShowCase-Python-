# Function - A block of reusable code 
#            Place () after the funtion name to invoke it.


# Argument
def happy_birthday(name, age):
    print(f"Happy birthday to you {name}")
    print(f"You are {age} years old")
    print("happy birthday to you!")
    print()

happy_birthday("Anny", 23)
happy_birthday("Aziz", 25)
happy_birthday("Himu", 30)

# Exercise - 1
print("\n======Exercise Code======.")
def display_invoice(username, amount, due_date):
    print(f"Hello! {username}.")
    print(f"Your bill of ${amount:.2f} is due: {due_date}.")

display_invoice("Karim", 85.90, "01/02")