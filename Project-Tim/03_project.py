import json

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

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_people(people)

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

def search(people):
    search_name = input("Search for a name: ").lower()
    result = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            result.append(person)

    display_people(result)

print("Hello!! Welcome to out Contact Managment System.\n")

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' & 'q' for quit: " ).lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("person added")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid Command!!")

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
