import random 
import string 

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters? (yes/no) ").strip().lower()
    include_special = input("Include special character? (yes/no) ").strip().lower()
    include_digits = input("Include digits? (yes/no) ").strip().lower()

    if length < 6:
        print("password length must be at least 6 character.")
        return 
    
    lower = string.ascii_lowercase
    #Inline if statement or a Ternary statement
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""

    #String concatenation 
    all_characters = lower + uppercase + special + digits

    required_character = []
    if include_uppercase == "yes":
        required_character.append(random.choice(uppercase))
    if include_special == "yes":
        required_character.append(random.choice(special))
    if include_digits == "yes":
        required_character.append(random.choice(digits))

    remaining_length = length - len(required_character)
    password = required_character

    for _ in range(remaining_length): #"_" is placeholder variable when you don't want to define something
        character = random.choice(all_characters)
        password.append(character)

    random.shuffle(password)

    str_password = "".join(password)
    return str_password


password = generate_password()
print(password)