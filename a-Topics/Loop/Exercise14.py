"""
🛒 Project — Supermarket Billing System (While Loop Version)
📋 Requirements-->

1️⃣ Keep running until user types "close" for customer name.
2️⃣ For each customer:
    Ask customer name.
    Keep entering item prices until "done" is typed.
    Calculate total bill.
    Apply discount:
        If total ≥ 5000 → 10% discount
        If total ≥ 2000 → 5% discount
        Otherwise → no discount
    Print final bill.
3️⃣ After closing the shop:
    Print:
        Total customers served
        Total revenue earned
        Customer with highest bill
        That highest bill amount
"""
total_customer = 0
total_revenue = 0

highest_bill = 0
customer_highest_bill = 0

while True:
    Customer_name = input("Enter customer name (or type 'close' to end): ").lower()

    if Customer_name == "close":
        break

    total_customer += 1
    total_bill = 0

    while True:
        price = input("Enter item price (or type 'done' to finish): ").lower()

        if price == "done":
            break

        price = float(price)
        total_bill += price

    # Apply discount
    if total_bill >= 5000:
        discount = total_bill * 0.10
    elif total_bill >= 2000:
        discount = total_bill * 0.05
    else:
        discount = 0

    final_bill = total_bill - discount

    print("Total bill = ",total_bill)
    print("Discount = ",discount)
    print("Final bill = ",final_bill)

    total_revenue += final_bill

    if final_bill > highest_bill:
        highest_bill = final_bill
        customer_highest_bill = Customer_name

print("\nShop closed.")
print("Total customer served = ",total_customer)
print("total revenue earned = ",total_revenue)
print("Customer with highest bill = ", customer_highest_bill)
print("That highest bill amount = ",highest_bill)