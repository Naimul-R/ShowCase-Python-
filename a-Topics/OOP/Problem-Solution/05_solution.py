# Polymorphism
class Car:
    # __init__ is `Constractor Mehtod`.
    def __init__(self, brand, model):
        # (__brand) this methods make this attribute privet
        self.__brand = brand
        self.model = model

    # Making getter method & Brand attribute privet
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

# Create an Inheritence class 
class ElectricCar(Car):
    def __init__(self, brand, model, bettary_size):
        # super() function is used inside a class to call methods or access properties from its parent (superclass)
        super().__init__(brand, model)
        self.bettary_size = bettary_size

my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
print(my_tesla.get_brand())

# my_car = Car("BMW", "X7 1")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name()) # full_name is function so perenthecis is required.

# my_new_car = Car("Audi", "Audi R8")
# print(my_new_car.model)