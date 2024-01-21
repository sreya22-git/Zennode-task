import math

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
        self.wrapped = False

    def calculate_total(self):
        return self.quantity * self.price

def apply_discount(subtotal, discount_rule, cart):
    if discount_rule == "flat_10_discount" and subtotal > 200:
        return 10
    elif discount_rule == "bulk_5_discount" and any(product.quantity > 10 for product in cart):
        return subtotal * 0.05
    elif discount_rule == "tiered_50_discount" and sum(product.quantity for product in cart) > 30 and any(product.quantity > 15 for product in cart):
        return sum(product.price * 0.5 * (product.quantity - 15) for product in cart if product.quantity > 15)
    elif discount_rule == "bulk_10_discount" and sum(product.quantity for product in cart) > 20:
        return subtotal * 0.10
    else:
        return 0

def main():
    products = [
        Product("Product A", 20),
        Product("Product B", 40),
        Product("Product C", 50)
    ]

    cart = []

    for product in products:
        quantity = int(input(f"Enter quantity for {product.name}: "))
        wrapped = input(f"Is {product.name} wrapped as a gift? (yes/no): ").lower() == "yes"

        product.quantity = quantity
        product.wrapped = wrapped
        cart.append(product)

    subtotal = sum(product.calculate_total() for product in cart)

    discount_rules = ["flat_10_discount", "bulk_5_discount", "bulk_10_discount", "tiered_50_discount"]
    discounts = [(rule, apply_discount(subtotal, rule, cart)) for rule in discount_rules]

    best_discount = max(discounts, key=lambda x: x[1])

    shipping_fee = math.ceil(sum(product.quantity for product in cart) / 10) * 5
    gift_wrap_fee = sum(1 for product in cart if product.wrapped) * 1

    total = subtotal - best_discount[1] + shipping_fee + gift_wrap_fee

    print("\nOrder Details:")
    for product in cart:
        print(f"{product.name}: Quantity - {product.quantity}, Total - ${product.calculate_total()}")
    print(f"\nSubtotal: ${subtotal}")
    print(f"Discount Applied: {best_discount[0]}, Amount: ${best_discount[1]}")
    print(f"Shipping Fee: ${shipping_fee}")
    print(f"Gift Wrap Fee: ${gift_wrap_fee}")
    print(f"\nTotal: ${total}")

if __name__ == "__main__":
    main()
