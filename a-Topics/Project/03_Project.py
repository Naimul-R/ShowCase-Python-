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

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
            return 
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transction_history.append(f"Withdraw : {amount}.")
        print(f"Withdraw: {amount}. Balance: {self.balance}.")

    def transfer(self, other, amount):
        print(f"\nTrensferring {amount} from {self.owner} to {other.owner}.")
        self.withdraw(amount)
        other.deposite(amount)

    def show_history(self):
        print(f"\nTransaction history for {self.owner}:")
        if not self.transction_history:
            print("No transection yet.")
            return 
        for entry in self.transction_history:
            print(f" {entry}")

    def __str__(self):
        return f"Account({self.owner}) | Balance {self.balance}."
    
acc1 = BankAccount("Mis. Sara", 5000)
acc2 = BankAccount("Mr. Naimul", 5500)

acc1.deposite(500)
acc1.withdraw(1000)

# transfer money 
acc1.transfer(acc2, 5000)

# Print the account dashboard
print(acc1)
print(acc2)

# show account history 
acc1.show_history()
acc2.show_history()