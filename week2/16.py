from abc import ABC,abstractmethod
class IShape:
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(IShape):
    def __init__(self,l,h):
        self.l=l
        self.h=h
    def calculate_area(self):
        print(f"Area of rectangle is {self.l*self.h}")
class Circle(IShape):
    def __init__(self,r):
        self.r=r
    def calculate_area(self):
        print(f"Area of circle is {self.r*self.r*3.14}")
r=Rectangle(10,20)
r.calculate_area()
c=Circle(10)
c.calculate_area()
