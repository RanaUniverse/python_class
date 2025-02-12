class Product:

    def __init__(self, price: float) -> None:
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, value: float):
        if value < 0:
            raise ValueError("Price Cannot Be Negative")

        self.__price = value


p1 = Product(10)
print(p1.get_price())
p1.set_price(999)
print(p1.get_price())
