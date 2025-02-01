class Employee:

    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    
    def print1(self):
        print(f"Name:{self.name}\nId:{self.id}\nDepartment{self.department}")

print("Enter the details of employee")
name=input("Enter Name")
id=input("Enter ID")
department=input("Enter Department")
obj=Employee(name,id,department)
obj.print1()