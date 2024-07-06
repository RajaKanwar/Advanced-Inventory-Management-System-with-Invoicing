
from inventory import Inventory
from product import Product

class InventoryManagement:
    def __init__(self):
        self.inventory = Inventory()

    def view_all_products(self):
        for product in self.inventory.view_products():
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}")

    def add_product(self, product_id, name, category, price, quantity):
        product = Product(product_id, name, category, price, quantity)
        self.inventory.add_product(product)

    def update_product(self, product_id, name=None, category=None, price=None, quantity=None):
        self.inventory.update_product(product_id, name, category, price, quantity)

    def remove_product(self, product_id):
        self.inventory.remove_product(product_id)