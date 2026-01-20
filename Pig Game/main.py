import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 playes.")
    else:
        ("Invalid! Try agian.")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:

    current_score = 0

    should_roll = input("Would you like to roll (y)? ")
    if should_roll.lower() != "y":
        break
        
    value = roll()
    if value == 1:
        print("You rolled a 1! Turn done!")
        break

    else:
        current_score += value
        print("You rolled a", value)

    print("Your score is: ",current_score)
