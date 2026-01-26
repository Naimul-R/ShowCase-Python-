import random
from words import words 
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choose a word from words list 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #What the user has guessed.

    lives = 10

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('you have', lives, ' lives left and you have used these letters: ', ' '.join(used_letters))

        # What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #Take away a life if wrong
                print("Letter is not in words")

        elif user_letter in used_letters:
            print("You have already used that charater. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # Gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("YAY! You guessed the word", word, "!!")


hangman()
