def get_number(number): 
    while True:
        operand = input(f"Number {number} : ")
        try:
            return float(operand)
        except:
            print("Invalid Number. Try again!")

operand = get_number(1)
operand2 = get_number(2)
sign = input("Sign: ")





