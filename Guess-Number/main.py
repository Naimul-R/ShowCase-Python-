import random

#Here we guess the number 
def guess(x):
    random_number = random.randint(1. x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too Low.")
        elif guess > random_number:
            print("Sorry, guess again. Too High.")

    print(f"Congratulations! You guessed the number {random_number} correctly!!")


#And in this define function computer guess the number.
def computer_guess(x):