class Inventory:
    def __init__(self):
        self.products = {} # this line calls Product.py 

    def add_product(self, product):
        self.products[product.product_id] = product # This line will call product.py and the product to be added will be added according to the point of product.py.

    def update_product(self, product_id, name=None, category=None, price=None, quantity=None):
        if product_id in self.products:
            if name:
                self.products[product_id].name = name
            if category:
                self.products[product_id].category = category
            if price:
                self.products[product_id].price = price
            if quantity is not None:
                self.products[product_id].quantity = quantity

    def remove_product(self, product_id): # First check the product ID. If it matches the product ID in the product list, then remove it.
        if product_id in self.products:
            del self.products[product_id]

    def view_products(self): # list of all product objects in the inventory.
        return self.products.values()
