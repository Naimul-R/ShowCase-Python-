import random
import json

def load_question():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]
        
    return questions

def get_random_questions(questions, num_questions):
    if num_questions > len(questions):
        num_questions = len(questions)
        
    random_questions = random.sample(questions, num_questions)
    return random_questions

def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(str(i + 1) + ".", option)
    
    numbers = int(input("Select the correct number: "))

question = load_question()
random_questions = get_random_questions(question, 2)
print(random_questions)