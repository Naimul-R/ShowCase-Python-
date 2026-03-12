def save_user(**user):
    print(user)

save_user(id=1, name="Naimul", number=12345)

# Exercise
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(15))