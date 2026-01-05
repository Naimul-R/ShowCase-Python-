def deposite():
    while True:
        Amount = input("What would you like to deposite? $")
        if Amount.isdigit():
            Amount = int(Amount)
            if Amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    return Amount 
