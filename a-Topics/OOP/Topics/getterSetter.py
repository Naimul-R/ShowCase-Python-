# Getter --> A getter is a method that reads and returns the value of a private attribute in a safe and controlled way.
class BankAccount:
    def __init__(self, text, balance):
        self.text = text
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
acc = BankAccount("Account Balance is = ", 150000)
print(acc.text, acc.balance)

