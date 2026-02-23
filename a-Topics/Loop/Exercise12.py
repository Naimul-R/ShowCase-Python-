"""
🌦 Exercise 12 — Weather Data Analyzer
📋 Requirements

1️⃣ Ask how many cities.
2️⃣ For each city:
    -Ask how many days of temperature data.
    -Enter temperature for each day.
    -Calculate:
        -Average temperature for that city
        -Number of “hot days” (temperature ≥ 35°C)
        -Number of “cold days” (temperature ≤ 10°C)
3️⃣ After all cities:
    -Print each city’s:
        -Average temperature
        -Hot day count
        -Cold day count
-Print which city had the highest average temperature.
-Print that highest average.
-If any city has more than 3 hot days → print:
    "Heatwave alert for City X"
"""
cities = int(input("Enter the number of cities: "))

average_list = []
hot_list = []
cold_list = []

highest_average = float('-inf')
hottest_city = 0

for i in range(1, cities + 1):
    print(f"\nCity {i}: ")

    days = int(input("Enter the number of days for temperature data: "))

    total_temp = 0
    hot_day = 0
    cold_day = 0

    for j in range(1, days + 1):
        temperature = float(input("Enter temperature for each day: "))

        total_temp += temperature

        if temperature >= 35:
            hot_day += 1
        if temperature <= 10:
            cold_day += 1

    if days > 0:
        average_tmep = total_temp / days
    else:
        average_tmep = 0

    average_list.append(average_tmep)
    hot_list.append(hot_day)
    cold_list.append(cold_day)

    # Track highest average
    if average_tmep > highest_average:
        highest_average = average_tmep
        hottest_city = i

# 🔎 AFTER ALL CITIES
print("\n--- Climate Report ---")

for i in range(cities):
    print(f"\nCity {i + 1}: ")
    print("Average temperature: ",round(average_list[i],2), "°C")
    print("Hot Days: ",hot_list[i])
    print("Cold Days: ",cold_list[i])

    if hot_list[i] > 3:
        print(f"\nHeatwave alert for city {i+1}")
    
print("\nCity with highest average temperature:", hottest_city)
print("Highest average temperature:", round(highest_average, 2), "°C")