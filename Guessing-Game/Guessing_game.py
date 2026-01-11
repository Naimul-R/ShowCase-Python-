import random 

easy_word = ["book", "tree", "flower", "apple", "game", "lion"]
medium_word = ["python", "planet", "calander", "pinaple", "stream", "bug-bounty"]
hard_word = ["aesthetic", "platue", "diamond", "computer", "minecraft", "pentesting"]

print("Welcome to the password guessing game")
print("Choose a difficulty level: Easy, Medium or Hard")

#Taking input level from user 
level = input("Enter your difficulty level: ").lower()
if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)
elif level == "hard":
    secret = random.choice(hard_word)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_word)

attempts = 0
print("\nGuess the secret password.")

while True:
    guess = input("Enter your guess: ")
    attempts += 1

    if guess == secret:
        print(f"Congratulation! You guessed it in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else: 
            hint += "_"

    print("Hint:", hint)

print("Game Over")
