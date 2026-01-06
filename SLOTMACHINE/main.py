MAX_LINES = 3

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

def get_number_of_lines():
    while True:
        Lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if Lines.isdigit():
            Lines = int(Lines)
            if 1 <= Lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return Lines


def main():
    balance = deposite()
    lines = get_number_of_lines()
    print(balance, lines)
main()
