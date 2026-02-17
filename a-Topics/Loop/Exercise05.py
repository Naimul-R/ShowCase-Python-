"""
Docstring for a-Topics.Loop.Exercise05
🎮 Task : Login System with Limited Attempts
📝 Task Instructions:

    • Set a correct password (hardcode it in the program)
    • Allow the user to enter the password
    • Use a while loop
    • If password is correct → print "Login Successful" and stop
    • If password is wrong → decrease remaining attempts
    • After 3 wrong attempts → print "Account Locked" and stop
"""
# create empty list.
password_storage = []

# Take password and store in empty list.
password_storage.append(input("Set your password: "))

attempts = 3

while attempts > 0:
    entered_password = input("Enter you login password: ")

    if password_storage[0] == entered_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Wrong password. Your attempts left:", attempts)

if attempts == 0:
    print("Account locked!")

