class Product:

    def __init__(self, price: float) -> None:
        self.__price = price
    def get_price(self):
        return self.__price
    def set_price(self, value: float):
        if value < 0:
            raise ValueError("Price Cannot Be Negative")
        self.__price = value

    price = property(get_price, set_price)

p1 = Product(10)
print(p1.get_price())
print("The Price is", p1.price)
p1.price = 999
print("The Updated Price is", p1.price)
