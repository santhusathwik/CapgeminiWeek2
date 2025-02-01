class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def speak(self):
        print("Dog woofs")
class Cat(Animal):
    def speak(self):
        print("Cat meows")

cat=Cat()
cat.speak()
dog=Dog()
dog.speak()