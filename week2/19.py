from abc import ABC,abstractmethod

class IVehicle:
    @abstractmethod
    def start_engine(self):
        pass
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("Car engine Started")
    def stop_engine(self):
        print("Car engine Stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine Started")
    def stop_engine(self):
        print("Bike engine Stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine Started")
    def stop_engine(self):
        print("Truck engine Stopped")
c=Car()
b=Bike()
t=Truck()
c.start_engine()
b.start_engine()
t.start_engine()
c.stop_engine()
b.stop_engine()
t.stop_engine()