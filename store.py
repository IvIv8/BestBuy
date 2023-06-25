from products import LimitedProduct


class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Invalid name")
        if price < 0:
            raise ValueError("Invalid price")
        if quantity < 0:
            raise ValueError("Invalid quantity")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if self.name == "Shipping" and quantity > 1:
            raise ValueError("Maximum order for that product is 1. Please enter the correct quantity")

        if quantity > self.quantity:
            raise Exception("Insufficient quantity")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


class Store:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        return self.products

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def order(self, shopping_list):
        total_price = 0
        shipping_count = 0

        for product, quantity in shopping_list:
            if product.name == "Shipping":
                shipping_count += 1
                if shipping_count > 1:
                    raise ValueError("Maximum order for that product is 1. Please enter the correct quantity.")
            total_price += product.buy(quantity)

        return total_price
