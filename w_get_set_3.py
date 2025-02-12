class Product:
    def __init__(self, price: float):
        self.__price = price  # Private

    @property
    def price(self):
        """Getter method"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """Setter method with validation"""
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value


# Example usage
product = Product(100)

print(product.price)  # ✅ Calls getter
product.price = 999  # ✅ Calls setter
print("New price of this product is,", product.price)
