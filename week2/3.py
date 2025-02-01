class Book:

    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
    
    def print1(self):
        print(f"Name:{self.title}\nId:{self.author}\nDepartment{self.isbn}")

book1=Book("The Aussies","Simon","123456")
book2=Book("The Kiwis","Tobi","9876")
book1.print1()
print("---------------------")
book2.print1()