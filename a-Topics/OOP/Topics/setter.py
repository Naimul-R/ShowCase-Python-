# Setter --> A setter is a method that changes or updates the value of a private attribute in a safe and controlled way.
class BankAccount:
    def __init__(self, text, balance):
        self.text = text
        self.__balance = balance  # private attribute (hidden)

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            print("Invalid! Cannot be negative.")
        else:
            self.__balance = new_balance # Only update if valid.

# Creating object 
acc = BankAccount("Account Balance = ", 150000)
print(acc.text, acc.balance)

# Updating balance (setter works here)
acc.balance = 2000000
print(acc.balance)

# Trying invalid value (setter blocks it)
acc.balance = -5000
print(acc.balance)
