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

print("Hello!! Welcome to out Contact Managment System.\n")
while True:
    command = input("You can 'Add', 'Delete' or 'Search' & 'q' for quit: " ).lower()
    people = []

    if command == "add":
        person = add_person()
        people.append(person)
        print("person added")
    elif command == "delete":
        pass
    elif command == "search":
        pass
    elif command == "q":
        break
    else:
        print("Invalid Command!!")


