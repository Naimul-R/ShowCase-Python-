# A simple program using functions that greets a person.

def full_greetings(name, age, city):
    print(f"Hello! {name}. You are {age} years old and you are from {city}.")

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city where you belong: ")

full_greetings(name, age, city);