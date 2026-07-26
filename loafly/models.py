import logging
from .transform import clean_price, apply_discount

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
            cleaned = clean_price(raw_price)
            if cleaned is None:
                logging.warning(f"Order {self.order_id}: skipping item '{name}' with missing price")
                continue
            total += cleaned
        return apply_discount(total)
