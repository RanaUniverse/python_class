class Car:
    total_cars = 0

    def __init__(self, brand:str, model:str):
        self.brand = brand
        self.model = model

        Car.total_cars += 1


car1 = Car("Toyota", "Carolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

print(f"Total Cars Created: {Car.total_cars}")

del car3
print(f"Total Cars Created: {Car.total_cars}")
