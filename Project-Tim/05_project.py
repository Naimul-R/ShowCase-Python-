import random
import json

def load_question():
    with open("questions.json", "r") as f:
        questions = json.load(f)["questions"]
        
    return questions