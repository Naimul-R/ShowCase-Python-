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

while attempt > MAX_ATTEMPT:
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