from time import *
import random as r

def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_start, time_end, userinput):
    time_delay = time_end - time_start
    time_round = round(time_delay, 2)
    speed = len(userinput) / time_round
    return round(speed)

test = [
    "Learning to type faster requires regular practice and focus.",
    "Typing speed improves when accuracy is given priority.",
    "Consistent effort helps build strong muscle memory.",
    "Simple exercises can increase confidence while typing.",
    "Good typing skills save time and improve productivity.",
    "Productivity increases when tasks are planned clearly.",
    "Managing time well helps reduce unnecessary stress.",
    "Focused work leads to better results in less time.",
    "Small daily improvements create long-term success.",
    "Discipline and consistency are key to staying productive.",
    "Effective time management allows individuals to prioritize important work, reduce distractions, and maintain steady progress throughout the day.",
    "Building productive habits requires patience, self-control, and a commitment to improving efficiency through regular practice and reflection.",
    "Technology connects people globally and enables faster communication across cultures, industries, and everyday digital experiences."
]

while True:
    test1 = r.choice(test)

    print("***** Typing Speed *****")
    print(test1)
    print()

    time_1 = time()
    test_input = input(" Enter: ")
    time_2 = time()

    print('Speed : ', speed_time(time_1, time_2, test_input)," w/sec")
    print("Error : ", mistake(test1, test_input))

    choice = input("Do you want to try again? (y/n): ")
    if choice.lower() != 'y':
        break