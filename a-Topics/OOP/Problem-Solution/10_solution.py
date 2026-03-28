# Class inheritance and isinstance() function

class Car:
    total_car = 0
    # __init__ is `Constractor Mehtod`.
    def __init__(self, brand, model):
        # (__brand) this methods make this attribute privet
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    # Making getter method & Brand attribute privet
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means to transport"
    
    @property
    def model(self):
        return self.__model

# Create an Inheritence class 
class ElectricCar(Car):
    def __init__(self, brand, model, bettary_size):
        # super() function is used inside a class to call methods or access properties from its parent (superclass)
        super().__init__(brand, model)
        self.bettary_size = bettary_size

    def fuel_type(self):
        return "Electric charge"

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))
# print(my_tesla.fuel_type())

# my_car = Car("Tata", "Safari")
# my_car.model = "city"
# Car("Tata", "Seadans")

# print(Car.general_description())
# print(my_car.model)

# my_car = Car("BMW", "X7 1")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name()) # full_name is function so perenthecis is required.

# my_new_car = Car("Audi", "Audi R8")
# print(my_new_car.model)

class battery: 
    def battery_info(self):
        return "lithium battery.🔋"
class engine:
    def engine_info(self):
        return "Iconic V8 engine.🤖"
    
class ElectricCarTwo(battery, engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model X")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())