class Person:
    def __init__(self,name):
        self.name=name

    def p_print(self,name):
        print(f"Person Name:{name}")


class Employee(Person):
    def __init__(self, name):
        self.name=name

    def e_print(self,name):
        print(f"Employee Name:{name}")


class Manager(Employee):
    def __init__(self, name):
        self.name=name
        self.print1(name)

    def print1(self,name):
        print(f"Manager Name:{name}")
    
    def approve_leave(self,name):
        print(f"{name} Leave has been approved")

o1=Manager("Rahul")
o1.e_print("JJ")
o1.p_print("Ethan")
o1.approve_leave("JJ")