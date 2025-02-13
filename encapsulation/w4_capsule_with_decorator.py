class Product:

    def __init__(self, price: float) -> None:
        self.__price = price  # Private Attribute

    @property
    def price(self):
        """Getter Method"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """This is setter methiods with validataion"""
        if value < 0:
            raise ValueError("Price Can't Be Negative")
        self.__price = value


p1 = Product(999)
print(p1.price)
p1.price = 99900
print(p1.price)
p1.price = -9