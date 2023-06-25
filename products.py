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
        self.set_quantity(quantity)


    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()


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

        if quantity > self.quantity:
            raise Exception("Insufficient quantity")

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)

        return total_price
