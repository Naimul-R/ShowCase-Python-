class Person:
    name = "Naimul"
    occupation = "Programmer"
    revenue = 150000

    def info(self):
        print(f"{self.name} is an {self.occupation}.")
    
a = Person()
b = Person()
c = Person()

a.name = "Alif"
a.occupation = "Accountant"
b.name = "Alvin"
b.occupation = "HR"

a.info()
b.info()
c.info()