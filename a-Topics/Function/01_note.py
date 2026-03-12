def get_greeting(name):
    return f"Hi! {name}"

message = get_greeting("Naimul")
file = open("Content.txt", "w")
file.write(message)

#Key word arguemt 
def increment(num, by):
    return num + by

print(increment(5, by=3)) # by=3 is key word argument.