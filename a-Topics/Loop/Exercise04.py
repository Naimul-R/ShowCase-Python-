"""
Docstring for a-Topics.Loop.Exercise04
🏧 Task : ATM Withdrawal System (While Loop)
• Ask the user to enter their initial bank balance
• Use a while loop to allow repeated withdrawals
• Each time:

    Ask how much money they want to withdraw

    If withdrawal amount is greater than balance → print "Insufficient balance"

    Otherwise → subtract it from balance
    • After each transaction, show remaining balance
    • Stop the loop if:

    Balance becomes 0

    OR user types "exit"
"""
balance = float(input("Enter your current balance: "))

while True:
    user_input = input("Enter withdrawal amount (or type 'exit'): ").lower()

    if user_input == "exit":
        print("Transaction is ended.")
        break

    withdrawal = float(user_input)

    if withdrawal > balance:
        print("In sufficient balance!")
    else:
        balance -= withdrawal
        print("Your remaining balance", balance)

    if balance == 0:
        print("Your balance is zero. You are not allowed for withdrawal.")
