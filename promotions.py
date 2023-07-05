from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        discounted_price = total_price - discount
        return discounted_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        # discounted_price = (product.price * (quantity // 2)) + (product.price * (quantity % 2))
        items_to_pay_half_price = quantity // 2
        items_to_pay_full_price = quantity - items_to_pay_half_price
        discounted_price = (items_to_pay_full_price + (items_to_pay_half_price * 0.5)) * product.price

        return discounted_price

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        free_quantity = quantity // 3
        return (quantity - free_quantity) * product.price