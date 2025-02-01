class Vehicle:
    def __init__(self,cost):
        self.cost=cost

    def show(self):
        print("This is vehicle class")
        
class Bike(Vehicle):
    def show(self):
        print("This is bike class - child of vehicle")
        print(f"Bike Price:{self.cost}")

class Car(Vehicle):
    def show(self):
        print("This is car class - child of vehicle")
        print(f"Car Price:{self.cost}")

class ElectricCar(Car):
    def show(self):
        print("This is electric car class - child of car")
        print(f"Electric Car Price:{self.cost}")


bus=Vehicle(100000)
pulsar=Bike(100)
bugatti=Car(1000)
hummer=ElectricCar(10000)
bus.show()
pulsar.show()
bugatti.show()
hummer.show()