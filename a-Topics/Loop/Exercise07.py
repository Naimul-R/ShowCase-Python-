"""
✅ Exercise 07: Cinema Ticket System
Ask how many shows
For each show:

    Ask how many seats
    For each seat:
        Ask if sold (yes/no)

Print sold seats per show
Print total sold tickets
Calculate total revenue (ticket price fixed at 300)
(3-level nested loop)
"""
shows = int(input("Enter how many shows are available: "))

total_ticket = 0
total_revenue = 0

for i in range(1, shows + 1):
    print(f"\nShows {i}")

    seat = int(input("Enter the available seat: "))

    for j in range(1, seat + 1):
        status = input("Is this seat sold (yes/no): ")
        