class Car:
    def move(self):
        super().move()
        print("Car Method")

class defAirplane:
    def move(self):
        print("defAirplane Method")

class FlyingCar(Car,defAirplane):
    def move(self):
        super().move()
        print("This is FlyingCar")

obj1=FlyingCar()
obj1.move()