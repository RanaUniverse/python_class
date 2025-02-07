class Vehicle:
    def __init__(self, brand: str, wheels: int):
        self.brand = brand
        self.wheels = wheels

    def display_info(self):
        print(f"Brand is: {self.brand}")
        print(f"Wheels is: {self.wheels}")


class Car(Vehicle):
    def __init__(self, brand: str, wheels: int, seating_capacity: int):
        super().__init__(brand, wheels)
        self.seating_capacity = seating_capacity

    def display_car_info(self):
        self.display_info()
        print(f"Seating capacity of this car is: {self.seating_capacity}")


class Bike(Vehicle):
    def __init__(self, brand: str, wheels: int, bike_type: str):
        super().__init__(brand, wheels)
        self.bike_type = bike_type

    def display_bike_info(self):
        self.display_info()
        print(f"Bike Type: {self.bike_type}")


car = Car("Toyota", 4, 5)

# car.display_info()

bike = Bike("Yamaha", 2, "Sports")
bike.display_bike_info()

bike.display_info()