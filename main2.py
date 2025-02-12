class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("BARK !!!")


class Cat(Animal):
    def speak(self):
        print("Meow !!!")


animals: list[Animal] = [Dog(), Cat()]

for animal in animals:
    animal.speak()
