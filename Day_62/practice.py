

class ShoppingCart:

    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Shopping Cart: {self.items}"

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)


cart1 = ShoppingCart(["Laptop", "Mouse"])
cart2 = ShoppingCart(["Keyboard", "Monitor"])

combined_cart = cart1 + cart2

print(cart1)
print(cart2)
print(combined_cart)
print("Total Items:", len(combined_cart))