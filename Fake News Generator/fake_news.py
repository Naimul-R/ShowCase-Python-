import random

#Create Subject
subjects = [
    "Ronaldo",
    "Messi",
    "Neymar",
    "Real Madrid",
    "Barcelona",
    "La Liga",
    "Premier League",
]

actions =[
    "wins the championship",
    "signs a new contract",
    "scores a hat-trick",
    "gets injured during training",
    "announces retirement",
    "not playing next season",
    "going to win major trophy"
]

places_or_things =[
    "at the final match",
    "in the transfer market",
    "during the press conference",
    "in the upcoming season",
    "at the training ground",
    "in the Club World Cup",
    "in the Champions League"
]

#Start the headline generation loops
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you generate another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#Print Goodbye message 
print("\nThank you for using the Fake News Generator. Goodbye!")
