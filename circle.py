import math
class Circle:
    def __init__(self, radius:float|int):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2