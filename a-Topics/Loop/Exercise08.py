"""
🏥 Exercise 8: Hospital Patient Billing System
📝 Task Instructions:

• Ask how many patients
• For each patient:
    Keep entering treatment cost
    Stop when user types "done"
        • Calculate total bill per patient
        • After all patients:

    Print total hospital revenue
    Print which patient had the highest bill
    Print the highest bill amount
"""
patients = int(input("Enter the number of patients have: "))

total_revenue = 0
patients_highest_bill = 0
highest_bill_amount = 0

for i in range(1, patients + 1):
    print(f"\nPatients {i}: ")

    patients_bill = 0

    while True:
        cost = input("Enter treatment cost (type 'done' to stop): ").lower()

        if cost == 'done':
            break
        
        cost = float(cost)
        patients_bill += cost

    print("Total bill for patients", i, "=", patients_bill)

    total_revenue += patients_bill

    # Check highest bill
    if patients_bill > highest_bill_amount:
        highest_bill_amount = patients_bill
        patients_highest_bill = i

print("\nTotal Hospital Revenue = ",total_revenue)
print("Patients with highest bill = ",patients_highest_bill)
print("Highest bill amount = ",highest_bill_amount)

