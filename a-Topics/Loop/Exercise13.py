"""
🏦 Exercise 13 — Bank Loan Risk Evaluation System
📋 Requirements
    1️⃣ Ask how many loan applicants.
    2️⃣ For each applicant:
        -Ask how many income sources they have.
        -Enter income amount for each source.
        -Calculate total monthly income.
        -Ask for credit score.
    3️⃣ Loan Approval Rules:
        -If total income ≥ 50,000 AND credit score ≥ 700 → Approved
        -If total income ≥ 30,000 AND credit score ≥ 600 → Conditionally Approved
        -Otherwise → Rejected
    4️⃣ After all applicants:
        Print:
            -Total approved applicants
            -Total rejected applicants
        -Print which applicant had the highest income.
        -Print that highest income.
        -If any applicant has income ≥ 100,000 → print:
            "High-value client detected: Applicant X"
"""
applicants = int(input("Enter the number of loan applicants: "))

approval_count = 0
rejection_count = 0

highest_income = 0
applicant_highest_income = 0

for i in range(1, applicants + 1):
    print(f"\nApplicant {i}: ")

    income_source = int(input("Enter the number of income sources: "))
    total_income = 0

    for j in range(1, income_source + 1):
        income_amount = float(input(f"Enter the income amount for sources {j}: "))
        total_income += income_amount

    credit_score = int(input("Enter the credit score: "))
    print("Total Monthly Income = ",total_income)

    #Loan Approval Rules
    if total_income >= 50000 and credit_score >= 700:
        print("Loan Status: Approved")
        approval_count += 1
    elif total_income >= 30000 and credit_score >= 600:
        print("Loan Status: Conditionally Approved")
        approval_count += 1
    else:
        print("Loan Status: Rejected")
        rejection_count += 1

    # Track highest income 
    if total_income > highest_income:
        highest_income = total_income
        applicant_highest_income = i

    # High-value client alert
    if total_income >= 100000:
        print(f"High-value client detected: Applicant {i}")

# Final Summary
print(f"\nTotal Approved Applicants: {approval_count}")
print(f"Total Rejected Applicants: {rejection_count}")
print(f"Applicant with highest income: Applicant: {applicant_highest_income}")
print(f"Highest Income: {highest_income}")