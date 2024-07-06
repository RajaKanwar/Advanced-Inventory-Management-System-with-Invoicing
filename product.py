class Product:
    def __init__(self, product_id, name, category, price, quantity):
        # Initialize the Product with given attributes
        self.product_id = product_id  # Unique identifier for the product
        self.name = name  # Name of the product
        self.category = category # Category to which the product belongs
        self.price = price # Price of the product
        self.quantity = quantity  # Quantity of the product in stock
