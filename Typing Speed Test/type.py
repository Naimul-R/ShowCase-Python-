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

def time_speed(time_start, time_end, timeinput):

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
    "Discipline and consistency are key to staying productive."
]
test1 = r.choice(test)

print("***** Typing Speed *****")
print(test1)
print()
print()

time_1 = time()
test_input = input(" Enter: ")
tine_2 = time()