"""
🚚 Exercise 11 — Delivery Performance Monitoring System
📋 Requirements

1️⃣ Ask how many drivers.
2️⃣ For each driver:
    -Ask how many deliveries they completed.
    -For each delivery:
        -Enter delivery time (in minutes).
        -Count how many deliveries were late.
        -Calculate average delivery time for that driver.
3️⃣ After all drivers:
    -Print each driver’s:
        -Average delivery time
        -Number of late deliveries
    -Print which driver had the lowest average delivery time.
    -Print that lowest average.
    -If any driver has more than 3 late deliveries → print:
        "Driver X needs performance review"
"""
drivers = int(input("Enter the number of drivers: "))

average_list = []
late_list = []

lowest_average = float('inf')
best_driver = 0

for i in range(1, drivers + 1):
    print(f"\nDriver {i}: ")

    deliveries = int(input("How many deliveries they complete: "))

    total_time = 0
    late_count = 0

    for j in range(1, deliveries + 1):
        time = int(input(f"Enter delivery time for delivery {j} (in minutes): "))
        total_time += time

        # Late delivery condition
        if time > 30:
            late_count += 1

    # Avoid devision by zero 0
    if deliveries > 0:
        average_time = total_time / deliveries
    else:
        average_time = 0

    average_list.append(average_time)
    late_list.append(total_time)

    # Find lowest average
    if average_time < lowest_average:
        lowest_average = average_time
        best_driver = i

# 🔎 AFTER all drivers
print("\n--- Final Driver Report ---")

for i in range(drivers):
    print(f"\nDrivers {drivers + 1}: ")
    print("Average delivery time:", round(average_list[i], 2), "minutes")
    print("Late deliveries:", late_list[i])

    if late_list[i] > 3:
        print(f"Driver {i+1} needs performance review")

# Print lowest average info 
print("\nDriver with the lowest average delivery time: ",best_driver)
print("Lowest average delivery time: ",round(lowest_average, 2), "minutes")