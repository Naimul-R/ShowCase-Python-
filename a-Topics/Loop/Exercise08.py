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

total_bill = 0

for i in range(1, patients + 1):
    print(f"\nPatients {i}: ")

    cost = (input("Enter treatment cost (type 'done' to stop): ")).lower()
    if cost == 'done':
        break