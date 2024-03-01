# products.py

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"{product.id}: {product.name} - ${product.price}")
