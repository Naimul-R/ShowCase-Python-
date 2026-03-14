"""
defination 1 - "Go through each player one by one,
                give each player a number starting from 1,
                print the number, name (neatly aligned), and score"
defination 2 -  enumerate simply adds a number to each item in the loop 💬 , 1 means start counting from 1 not 0

":<10" means --> :<10 simply means give this word 10 spaces so everything lines up neatly,
                For example--> 1. Ali        - Score: 95
                               2. Sara       - Score: 88
"""
players = [
    {"name": "Ali",   "score": 95},
    {"name": "Sara",  "score": 88},
    {"name": "Ahmed", "score": 72}
]

for i, player in enumerate(players, 1):
    print(f"{i}. {player['name']:<10} - Score: {player['score']}")



