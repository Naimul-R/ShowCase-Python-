# while loop = Execute some code WHILE some condition remain true.

# Example - 1
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")

# Example - 2
age = int(input("Enter your age: "))

while age < 0:
    print("Your age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

# Example - 3
food = input("Enter the food you like (q to quite): ")

while not food == "q":
    print(f"you like {food}")
    food = input("Enter another food that you like (q to quite): ")

print("Goodbye!")

# Example - 4
num = int(input("Enter a number between (1 - 10): "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between (1 - 10): "))

print(f"You number is {num}")
