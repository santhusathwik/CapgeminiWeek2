from abc import ABC,abstractmethod

class ICalculator:
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
    @abstractmethod
    def mul(self):
        pass
    def div(self):
        pass

class Calculator(ICalculator):
    def add(self,a,b):
        self.a=a
        self.b=b
        print(f"The sum is {a+b}")
    def sub(self,a,b):
        self.a=a
        self.b=b
        print(f"The difference is {a-b}")
    def mul(self,a,b):
        self.a=a
        self.b=b
        print(f"The product is {a*b}")
    def div(self,a,b):
        self.a=a
        self.b=b
        print(f"The result is {a/b}")
c=Calculator()
c.add(10,20)
c.sub(10,20)
c.mul(10,20)
c.div(10,20)