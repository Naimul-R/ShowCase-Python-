# Wake up function 
def wake_up(name, time):
    print(f"{name} woke up at {time}.")

# Meal Tracker function
def meal_tracker(name, meal, food):
    print(f"{name} has breakfast - {meal} and {food}")

# Exercise Tracker function 
def exercise_tracker(name, exercise, duration):
    print(f"{name} did {exercise} for {duration}")

# sleep tracker function 
def sleep_tracker(name, sleep_time):
    print(f"{name} went to sleep at {sleep_time}. Good night! 🌙")


# --- User Input ---
name = input("Enter your name: ")
time = input("Enter wake up time: ")
meal = input("Enter meal type (Breakfast/Lunch/Dinner): ")
food = input("Enter food name: ")
exercise = input("Enter exercise name: ")
duration = input("Enter duration (in minutes): ")
sleep_time = input("Enter sleep time: ")

# --- Calling the functions ---
wake_up(name, time)
meal_tracker(name, meal, food)
exercise_tracker(name, exercise, duration)
sleep_tracker(name, sleep_time)