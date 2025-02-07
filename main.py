class Vehicle:
    def __init__(
        self,
        brand: str = "Local",
        wheels: int = 4,
    ):
        self.brand = brand
        self.wheels = wheels

    def display_info(self):
        print(f"This is Boss Class's display info")
        print(f"The Brand is: {self.brand}")
        print(f"The numbers of Wheels are: {self.wheels}")
