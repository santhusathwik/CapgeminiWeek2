class Product:

    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    
    def check_availability(self,quantity):
        if(quantity>self.stock):
            print("The quantity is unavailable")
        else:
            print("The quantity is available")


kurkure=Product("kurkure",55,100)
lays=Product("lays",40,250)
bingo=Product("bingo",100,70)
print("1-Kurkure\n2-Lays\n3-Bingo")
choice=int(input("Enter the choice"))
quantity=int(input("Enter the quantity"))
if choice==1:
    kurkure.check_availability(quantity)
elif choice==2:
    lays.check_availability(quantity)
elif choice==3:
    bingo.check_availability(quantity)
else:
    print("Please enter correct option")