"""
🚦 Project — Smart Parking Lot Management System
"""
capacity = int(input("Enter total parking capacity: "))

occupied_slot = 0
total_entries = 0
total_exit = 0
peak_occupency = 0

while True:
    print("\n--- Parking Managment Menu ---")
    print("1. Car Entry.")
    print("2. Exit.")
    print("3. View Parking Status.")
    print("4. Close Parking")

    choice = input("Enter your choice: ")

    # 1- car Entry
    if choice == "1":
        car_plate = input("Enter your plate number: ")

        if occupied_slot > capacity:
            print("Parking Full — Entry Denied")
        else:
            occupied_slot += 1
            total_entries += 1

            if occupied_slot > peak_occupency:
                peak_occupency = occupied_slot

            print("Car", car_plate, "Entered successfully")
            print("current occupied slot =", occupied_slot)

    # Car Exit
    if choice == "2":
        car_plate = input("Enter the car plate number: ")

        if occupied_slot <= 0:
            print("Parking Empty.")
        else:
            occupied_slot -= 1
            total_exit += 1

            print("Car", car_plate, "exit successfully!")
            print("Current occupied slot = ", occupied_slot)

    # View Parking status 
    if choice == "3":
        print("\nParking Status...")
        print("Total Capacity = ", capacity)
        print("Currently Occupied Slot = ", occupied_slot)
        print("Available slot = ", capacity - occupied_slot)
        print("Total car entered today = ", total_entries)
        print("Peak occupecy today = ", occupied_slot)

    # close Parking 
    if choice == "4":
        print("\nClosing parking system...")
        print("\n---- Final Report ----")
        print("Total car entry = ", total_entries)
        print("Total exites = ", total_exit)
        print("Peak occupecy = ", peak_occupency)
        print("final Occupied slot = ", occupied_slot)
        break
    else:
        print("Invalid choice. Please enter (1-4).")
