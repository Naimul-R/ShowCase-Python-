class Car:
    # __init__ is `Constractor Mehtod`.
    def __init__(self, brand, model):
        # Brand & model are `Attribute`
        self.brand = brand
        self.model = model

my_car = Car("BMW", "BMW X7 1")
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Audi", "Audi R8")
print(my_new_car.model)