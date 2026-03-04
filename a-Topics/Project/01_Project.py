"""
🏨 Smart Hotel Booking Management System
"""
# ==================================================
# SMART HOTEL BOOKING MANAGEMENT SYSTEM
# ==================================================

# ----------------------------
# ADMIN LOGIN SYSTEM
# ----------------------------
ADMIN_USERNAME = "admin"
ADMIN_PASS = "1234509"
MAX_ATTEMPT = 3
attempt = 0

while attempt < MAX_ATTEMPT:
    print("\n====== ADMIN LOGIN ======")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username == ADMIN_USERNAME and password == ADMIN_PASS:
        print("Login successfull\n")
        break
    else:
        attempt += 1
        print(f"Invalid credential. Attempts left: {MAX_ATTEMPT - attempt}")
else:
    print("Too many failed attempt. System locked.")
    exit()

# ==================================================
# HOTEL SYSTEM STARTS
# ==================================================
# Fixed room type
room_type = ("Single", "Double", "Suite", "Deluxe")

# Pricing Congfiguration Dictonary 
room_prices = {
    "single": 1000,
    "double": 1500,
    "suite": 2000,
    "deluex": 4550,
}

SERVICE_COST = 20

# Data Storage
guests = set()
bookings = {}

# ==================================================
# MAIN MENU LOOP
# ==================================================
while True:
    print("\n=================================")
    print("SMART HOTEL BOOKING SYSTEM")
    print("=================================")
    print("1. View room type")
    print("2. Register Guest")
    print("3. Create Booking")
    print("4. Add extra services")
    print("5. View booking report")
    print("6. Cancel Booking")
    print("7. Exit.")

    choice = input("Select option (1-7): ").strip()

    # ---------------------------------
    # Option 1 — View Room Types
    # ---------------------------------
    if choice == "1":
        print("\nAvailable room type:")
        for room in room_type:
            print("-", room)

    # ---------------------------------
    # Option 2 — Register Guest
    # ---------------------------------
    elif choice == "2":
        name = input("Enter the guest name for register: ").strip().title()

        if name in guests:
            print("Guest already registerd.")
        else:
            guests.add(name)
            print("Guest registered successfully.")

    # ---------------------------------
    # Option 3 — Create Booking
    # ---------------------------------
    elif choice == "3":
        name = input("Enter guest name: ").strip().title()

        if name not in guests:
            print("Guest does not exit.")
        else:
            room = input("Enter room type: ").strip().title()

            if room not in room_type:
                print("Invalid room type. Try agian!")
            else:
                nights = int(input("Enter number of night: "))

                bookings[name] = {
                    "room_type": room,
                    "nights": nights,
                    "services": []
                }

                print("Booking Create Successfully.")

    # ---------------------------------
    # Option 4 — Add Extra Services
    # ---------------------------------
    elif choice == "4":
        name = input("Enter the guest name: ").strip().title()

        if name not in bookings:
            print("No bookings found for this guest.")
        else:
            service = input("Enter service (Breakfast/WiFi/Spa/Airport Pickup): ").strip().title()
            bookings[name]["services"].append(service)
            print("Service added successfully!")

    # ---------------------------------
    # Option 5 — View Booking Report
    # ---------------------------------
    elif choice == "5":
        if not bookings:
            print("No bookings available.")
        else:
            print("\n--------- BOOKING REPORT ---------")

            highest_payment = 0
            top_guest = None

            for guest, info in bookings.items():
                room = info["room_type"]
                nights = info["nights"]
                services = info["services"]

                room_cost = room_prices[room] * nights
                service_cost = len[services] * SERVICE_COST
                total_cost = room_cost + service_cost

                print(f"\nGuest: {guest}")
                print("Room: ", room)
                print("Nights: ", nights)
                print("Services: ", services)
                print("Total cost: ", total_cost)

                if total_cost > highest_payment:
                    highest_payment = total_cost
                    top_guest = guest

            print("\nHighest paying guest: ", top_guest)
            print("Amount: ", highest_payment)

    # ---------------------------------
    # Option 6 — Cancel Booking
    # ---------------------------------
    elif choice == "6":
        name = input("Enter guest name to cancel bookings: ").strip().title()

        if name in bookings:
            bookings.pop(name)
            print("Bookings cancelled successfully!")
        else:
            print("Booking not found!")

    # ---------------------------------
    # Option 7 — Exit
    # ---------------------------------
    elif choice == "7":
        print("Existing system. GoodBye!")
        break
    else:
        print("Invalid chocie. Select (1-7).")
