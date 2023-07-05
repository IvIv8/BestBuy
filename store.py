from products import LimitedProduct

class Store:
    def __init__(self, products):
        self.products = products


    def get_all_products(self):
        return self.products


    def display_products(self):
        if not self.products:
            print("No products available in the store.")
            return

        for index, product in enumerate(self.products, start = 1):
            print(f"{index}. {product}")


    def get_total_quantity(self):
        total_quantity = 0
        for p in self.products:
            total_quantity += p.get_quantity()
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
