class Electronics:
    def __init__(self,num):
        self.num=num   

    def show(self):
        print("This is Electronics")
        print(f"The total products are {self.num}")

class MobileDevice(Electronics):
    def __init__(self,num):
        super().__init__(num)
        self.num-=6

    def show(self):
        print("This is MobileDevice")
        print(f"The total products are {self.num}")

class SmartPhone(MobileDevice):
    def __init__(self,num):
        super().__init__(num)
        self.num-=2

    def show(self):
        print("This is SmartPhone")
        print(f"The total products are {self.num}")

obj=SmartPhone(10)
obj.show()