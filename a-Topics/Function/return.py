# return = statement used to end a function.
#            and send a result back to the caller.

def add(x, y):
    z = x + y
    return z

def subtrack(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(2, 4))
print(subtrack(2, 4))
print(multiply(2, 4))
print(divide(2, 4))

# Exercise: 
print("\n===== Exercise =====")
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Naimul", "Rabby")
print(full_name)