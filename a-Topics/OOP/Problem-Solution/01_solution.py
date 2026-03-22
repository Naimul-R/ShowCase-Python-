class Car:
    def __init__(self, brand, model):
        # Brand & model are `Attribute`
        self.brand = brand
        self.model = model

my_car = Car("BMW", "BMW X7 1")
print(my_car.brand)