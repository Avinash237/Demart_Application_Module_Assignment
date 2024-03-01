# cart.py

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, product_id):
        for item in self.items:
            if item.product.id == product_id:
                self.items.remove(item)
                return True
        return False

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        return total

    def display_cart(self):
        print("Shopping Cart:")
        for item in self.items:
            print(f"{item.product.name} - Quantity: {item.quantity}")
        print(f"Total: ${self.calculate_total()}")
