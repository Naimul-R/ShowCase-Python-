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
room_price = {
    "single": 1000,
    "Double": 1500,
    "Suite": 2000,
    "Deluex": 4550,
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

