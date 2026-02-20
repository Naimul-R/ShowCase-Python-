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
highest_ticket = 0
best_show = 0

ticket_price = float(input("Enter ticket price: "))

for i in range(1, shows + 1):
    print(f"\nShows {i}")

    seat = int(input("Enter the available seat: "))
    show_ticket = 0

    for j in range(1, seat + 1):
        status = input("Is this seat sold (yes/no): ").lower()

        if status == "yes":
            show_ticket += 1
            total_ticket += 1
            total_revenue += ticket_price

    print("Tickets sold in this show: ",show_ticket)

    #Check highest selling show 
    if show_ticket > highest_ticket:
        highest_ticket = show_ticket
        best_show = i

print("\nTotal ticket sold: ",total_ticket)
print("Total revenue: ",total_revenue)
print("Best show: ",best_show)
print("Highest Tickets sold in a show: ",highest_ticket)
