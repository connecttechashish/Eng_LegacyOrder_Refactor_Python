from .transform import clean_price, apply_discount
from .config import DISCOUNT_PERCENT

class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, name, raw_price):
        self.items.append((name, raw_price))

    def total(self):
        total = 0
        for name, raw_price in self.items:
            total += clean_price(raw_price)
        return apply_discount(total, DISCOUNT_PERCENT)
