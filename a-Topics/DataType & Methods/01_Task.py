"""
Task 1 — STRING Methods (Fundamental Level)
Building a mini username analyzer for a system-->
The program should:
    1-Ask the user to enter a sentence.
    2-Remove extra spaces from both sides.
    3-Convert the sentence to:
        All lowercase
        Title case
    4-Replace all spaces with underscores.
    5-Count how many times the letter 'a' appears.
    6-Find the position of the first 'e'.
    7-Check:
        Does it start with "hello"?
        Does it end with "."?
    8-Print all results clearly.
"""
# Step 1: Ask the user to enter a sentence
sentence = input("Please enter a sentence: ")

#Remove extra space 
cleaned_sentence = sentence.strip()

# Convert the sentence all lowercase
lower_sentence = cleaned_sentence.lower()

# TitleCase 
title_sentence = cleaned_sentence.title()

# Replace spaces with underscore (_)
underscore_sentence = title_sentence.replace(" ", "_")

# Count latter a 
count_a = lower_sentence.count("a")

# Find the position of "e"
e_position = lower_sentence.find("e")

# Check if starts with "hello" (case insensitive)
check_hello_sen = lower_sentence.startswith("hello")

# check if end with "."
check_end_sen = cleaned_sentence.endswith(".")

# Print result
print("\nCleaned Sentence = ", cleaned_sentence)
print("Lowercase:", lower_sentence)
print("Title case:", title_sentence)
print("Underscore version:", underscore_sentence)
print("Count of 'a':", count_a)
print("First position of 'e':", e_position)
print("Starts with 'hello':", check_hello_sen)
print("Ends with '.':", check_end_sen)