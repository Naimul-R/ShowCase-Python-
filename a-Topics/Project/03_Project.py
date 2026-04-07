class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transction_history = []

    def deposite(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return 
        self.balance += amount
        self.transction_history.append(f"Deposite : {amount}")
        print(f"Deposited {amount}. Balance : {self.balance}.")
