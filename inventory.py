class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

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

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def view_products(self):
        return self.products.values()