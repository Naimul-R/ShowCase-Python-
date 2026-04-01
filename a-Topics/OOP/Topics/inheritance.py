# Inheritance --> Inheritance is when a child class automatically gets all the properties and methods of a parent class without rewriting them.
# Parent class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand 
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h.")

    def stop(self):
        print(f"{self.brand} has stopped.")

# CHILD CLASS 1 — inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, speed, door):
        super().__init__(brand, speed)  # calling parent constructor
        self.door = door

    def honk(self):
        print(f"{self.brand} car is honking! 📯 It has {self.door} doors.")

# CHILD CLASS 2
class Truck(Vehicle):
    def __init__(self, brand, speed, capacity):
        super().__init__(brand, speed)
        self.capacity = capacity

    def load(self):
        print(f"{self.brand} truck is loading {self.capacity} tons of goods. 🚛")


car = Car("Toyota", 120, 4)
truck = Truck("Volvo", 80, 20)

# car
car.move()
car.stop()
car.honk()

print()
# truck 
truck.move()
truck.stop()
truck.load()