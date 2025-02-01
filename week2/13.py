class Shape:
    def area1(self,area):
        self.area=area
        print(f"The area is {area}")

class Square(Shape):
    def area1(self,s):
        area=s*s
        super().area1(area)

class Triangle(Shape):
    def area1(self,l,h):
        area=0.5*l*h
        super().area1(area)

sq=Square()
sq.area1(10)
tr=Triangle()
tr.area1(10,5)
