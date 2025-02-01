class BankAccount:

    def __init__(self,balance):
        self.balance=balance
    
    def print1(self):
        print(f"Balance:{self.balance}\n")

    def withdraw(self,money):
        if(self.balance>=money):
            self.balance-=money
            print(F"Balance{self.balance}")
        else:
            print("Insufficient Funds")
    
    def deposit(self,money):
        self.balance+=money
        print(F"Balance{self.balance}")

balance=int(input("Enter the intial balance"))
bank=BankAccount(balance)
print("1-withdraw\n2-deposit")
n=int(input("Enter the choice"))
if n==1:
    money=int(input("Enter the money to be withdrawn"))
    bank.withdraw(money)
elif n==2:
    money=int(input("Enter the money to be deposited"))
    bank.deposit(money)
    
else:
    print("Please enter the correct option")
    

