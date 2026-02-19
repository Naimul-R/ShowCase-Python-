"""
✅ Exercise 6: Daily Expense Tracker

Ask how many days to track
For each day:

    Keep entering expenses until user types "done"
    Calculate total for that day

After all days:

    Print highest spending day
    Print overall total expense
    (While + nested + max tracking)
"""
Day = int(input("Enter the number of days you want to track: "))

overall_total = 0
highest_day_total = 0
highest_day = 0

for i in range(1, Day + 1):
    print(f"\nDay {i}: ")

    daily_total = 0

    while True:
        expenses = (input("Enter expense amount (or type 'done'): ")).lower()

        if expenses == 'done':
            break

        expenses = float(expenses)
        daily_total += expenses

    print("Total expence for the day", i, "=", daily_total)

    overall_total += daily_total

    # Check highest spending day 
    if daily_total > highest_day_total:
        highest_day_total = daily_total
        highest_day = i

print("Overall total expenses = ",overall_total)
print("Highest spending day = ",highest_day)
print("Highest day expenses = ",highest_day_total)