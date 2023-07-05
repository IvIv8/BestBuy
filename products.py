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
        if quantity > 0:
            self.active = True
        else:
            self.active = False

        self.promotion = None


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


    def set_promotion(self, promotion):
        self.promotion = promotion


    def __str__(self):
        promotion_info = f"No promotion" if self.promotion is None else f"Promotion: {self.promotion.name}"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"


    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if self.name == "Shipping" and quantity > 1:
            raise ValueError("Maximum order for that product is 1. Please enter the correct quantity")

        if quantity > self.quantity:
            raise Exception("Insufficient quantity")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity = 0)

    # def set_promotion(self, promotion):
    #    raise ValueError("Non-stocked products cannot have promotions.")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, max_quantity = 1):
        super().__init__(name, price, quantity)
        self.max_quantity = max_quantity
        self.purchased_quantity = 0


    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")

        if quantity > self.quantity or (self.purchased_quantity + quantity) > self.max_quantity:
            raise Exception("Maximum order for that product is 1. Please enter the correct quantity.")

        total_price = self.price * quantity
        self.quantity -= quantity
        self.purchased_quantity += quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


# Example usage
def example_funct():
    non_stocked_product = NonStockedProduct("Windows License", price=125)
    limited_product = LimitedProduct("Shipping", price=10, quantity=250, max_quantity=1)

    print(non_stocked_product.show())  # Windows License, Price: 125, Quantity: 0, No promotion
    print(limited_product.show())  # Shipping, Price: 10, Quantity: 250, No promotion
