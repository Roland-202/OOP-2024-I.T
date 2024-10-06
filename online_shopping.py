class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: ${self.price}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")

class ShoppingCart:
    total_carts = 0

    def __init__(self):
        self.items = []
        # adds to idems in a cart
        ShoppingCart.total_carts += 1        

    def add_to_cart(self, product, quantity):
        if quantity > product.quantity_in_stock:
            print(f"Insufficient stock for {product.product_name}.")
        else:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"{quantity} {product.product_name} added to cart.")

    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                print(f"{item[1]} {product.product_name} removed from cart.")
                break
        else:
            print(f"{product.product_name} not found in cart.")

    def display_cart(self):
        print("Cart Contents:")
        if not self.items:
            print("Cart is empty.")
        else:
            for item in self.items:
                print(f"{item[1]} x {item[0].product_name} - ${item[0].price * item[1]}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total

# theses are the Products 
product1 = Product("iphone 16", 1200, 10)
product2 = Product("ps5 pad", 35, 20)
product3 = Product("Red Bull", 5, 300)

# these are Shopping Cart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add items to carts
cart1.add_to_cart(product1, 1)
cart1.add_to_cart(product2, 2)
cart2.add_to_cart(product3, 4)
cart2.add_to_cart(product1, 2)

# this Displays cart contents and calculates total
print(f"\nCart 1:")
cart1.display_cart()
print(f"Total: ${cart1.calculate_total()}")

print(f"\nCart 2:")
cart2.display_cart()
print(f"Total: ${cart2.calculate_total()}")