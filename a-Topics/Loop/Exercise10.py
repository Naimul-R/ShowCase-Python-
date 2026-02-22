"""
🎮 Exercise 10 — Gaming Tournament Tracker.
📋 Requirements
    1️⃣ Ask how many teams are participating.
    2️⃣ For each team:
        -Ask how many matches they played.
        -For each match:
            Input result (win, draw, loss)
            Calculate total points for that team.
    3️⃣ After all teams:
        -Print total points for each team.
        -Print which team has the highest points.
        -Print that highest point.
        -If any team has 0 total points → print
            ("Team X eliminated — no points earned")
"""
Team = int(input("Enter the number of teams are participant: "))

team_highest_point = 0
best_team = 0

for i in range(1, Team + 1):
    print(f"\nTeam {i}: ")

    match = int(input("Enter the number of matches they played: "))
    total_point = 0

    for j in range(1, match + 1):
        result = input("Enter the result of this game (win/draw/loss): ").lower()

        if result == "win":
            total_point += 3
        elif result == "draw":
            total_point += 1
        elif result == "loss":
            total_point += 0
        else:
            print("Invalid Input. Try again!")

    print(f"Total point for Team {i} :",total_point)

    # Elemination Condition
    if total_point == 0:
        print(f"Team {i} eliminated - no point earned!")

    # Get which team has highest point
    if total_point > team_highest_point:
        team_highest_point = total_point
        best_team = i 

# Printing the required output -->
print("\nTeam with highest point = ", best_team)
print("Highest points = ",team_highest_point)
