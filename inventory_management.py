
from inventory import Inventory
from product import Product

class InventoryManagement:
    def __init__(self):
        self.inventory = Inventory()

    def view_all_products(self):
        for product in self.inventory.view_products():
            # Printing the details of each product
            print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}")

    def add_product(self, product_id, name, category, price, quantity):
        product = Product(product_id, name, category, price, quantity)  # Adding the created product to the inventory using the add_product method of the Inventory class
        self.inventory.add_product(product)

    def update_product(self, product_id, name=None, category=None, price=None, quantity=None):
        self.inventory.update_product(product_id, name, category, price, quantity) # Updating the product in the inventory using the update_product method of the Inventory class

    def remove_product(self, product_id):
        self.inventory.remove_product(product_id)
