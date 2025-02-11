from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def number_of_wheels(self) -> int:
        """This is for as this has alwasy need to have wheel in all vehicle"""
        pass


class Car(Vehicle):
    def number_of_wheels(self):
        return 4


class Bike(Vehicle):

    def number_of_wheels(self) -> int:
        return 2


class Truck(Vehicle):
    def number_of_wheels(self) -> int:
        return 6


vehicles: list[Vehicle] = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    print(f"All {vehicle.__class__.__name__} has {vehicle.number_of_wheels()} wheels.")

