# main.py
from products import Product, ProductCatalog
from Cart import CartItem, ShoppingCart

def main():
    catalog = ProductCatalog()
    cart = ShoppingCart()

    # Adding some sample products
    catalog.add_product(Product(1, "Shirt", 20))
    catalog.add_product(Product(2, "Pants", 30))
    catalog.add_product(Product(3, "Shoes", 50))

    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Remove from Cart\n5. Checkout\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            catalog.display_products()

        elif choice == '2':
            product_id = int(input("Enter the product ID to add to cart: "))
            product = catalog.get_product_by_id(product_id)
            if product:
                quantity = int(input("Enter the quantity: "))
                cart.add_item(CartItem(product, quantity))
                print("Product added to cart.")
            else:
                print("Product not found.")

        elif choice == '3':
            cart.display_cart()

        elif choice == '4':
            product_id = int(input("Enter the product ID to remove from cart: "))
            if cart.remove_item(product_id):
                print("Product removed from cart.")
            else:
                print("Product not found in cart.")

        elif choice == '5':
            print("Thank you for shopping with us!")
            break

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
