# Constractor --> A constructor is a special method that is automatically called when an object is created from a class. It initializes the object's attributes and sets up its initial state.

class Person: 
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        print(f"Hey! I am {self.name}")

    def info(self):
        print(f"{self.name} is an {self.occupation}.")

a = Person("Naimul", "Developer")
b = Person("Akash", "HR")

a.info()
b.info()

