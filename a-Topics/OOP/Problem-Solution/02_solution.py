class Car:
    # __init__ is `Constractor Mehtod`.
    def __init__(self, brand, model):
        # Brand & model are `Attribute`
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

my_car = Car("BMW", "X7 1")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name()) # full_name is function so perenthecis is required.

my_new_car = Car("Audi", "Audi R8")
print(my_new_car.model)