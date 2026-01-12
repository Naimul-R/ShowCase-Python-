import random 

questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3",
    "Which keyword is used to create a class in Python?": "class",
    "Which function is used to display output in Python?": "print",
    "What symbol is used for assignment in Python?": "=",
    "Which data type is used to store whole numbers?": "int",
    "Which data type is used to store decimal numbers?": "float",
    "Which keyword is used to check a condition in Python?": "if",
    "Which keyword is used to handle exceptions?": "try",
    "What keyword is used to define a loop that runs while a condition is true?": "while",
    "Which keyword is used to stop a loop?": "break",
    "Which keyword is used to skip the current iteration of a loop?": "continue",
    "What function converts a value to an integer?": "int",
    "What function converts a value to a string?": "str",
    "Which data type is used to store multiple items in a single variable?": "list",
    "Which data type stores key–value pairs?": "dictionary",
    "What keyword is used to return a value from a function?": "return"
}

def python_trivia_game():
    questions_list = list(questions.keys()) #Using .key() to get the output of key or ,value()
    total_questions = 8
    score = 0

    selected_questions = random.sample(questions_list, total_questions)
    
    for idx, question in enumerate(selected_questions): #Enumerate will gives us     index as well the value.
        print(f"{idx + 1}. {question}")
        user_answer = input("Your Answer: ").lower().strip()
        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {correct_answer}.\n")

    print(f"Game Over! Your finel score is: {score}/{total_questions}")


python_trivia_game()