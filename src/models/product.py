"""Product model representing an item in the pet store."""

class Product:
    def __init__(self, id: int, name: str, category: str, price: float, stock: int):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def is_in_stock(self) -> bool:
        return self.stock > 0

    def __repr__(self):
        return f"<Product {self.id}: {self.name} (${self.price})>"
