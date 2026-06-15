def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name": name,
        "age": age,
        "email": email
    }
    return person

def delete_contact(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of number!!")
            else:
                break
        except:
            print("Invalid Number")

    people.pop(number - 1)
    print("Person deleted.")

print("Hello!! Welcome to out Contact Managment System.\n")

people = []

while True:
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' & 'q' for quit: " ).lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("person added")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("Invalid Command!!")


