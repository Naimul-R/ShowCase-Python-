# 1. Get balance function
def get_balance(income, expences):
    balance = income - expences
    return balance 

# 2. Safety checker function
def is_safe(balance):
    if balance > 3000:
        return "You are financially safe! ✅"
    elif balance >= 1000:
        return "Be careful with spending! ⚠️"
    else:
        return "Warning! Low balance! 🚨"
    
# 3. Save money function
def save_money(balance, saving_percent):
    saving = balance * saving_percent / 100
    return saving 

# 4. Full report function
def full_report(name, income, expences, saving_percent):
    # Calling all function 
    balance = get_balance(income, expences)
    status = is_safe(balance)
    savings = save_money(balance, saving_percent)

    # --- Printing the report ---
    print("--- Money Report ---")
    print("Name = ", name)
    print("Income = ", income)
    print("Expences = ", expences)
    print("Balance = ", balance)
    print("Status = ", status)
    print("You should save = ", savings)

# --- User Input ---
name           = input("Enter your name: ")
income         = int(input("Enter your income: "))
expenses       = int(input("Enter your expenses: "))
saving_percent = int(input("Enter saving percent: "))

# --- Calling the function ---
full_report(name, income, expenses, saving_percent)