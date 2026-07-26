import csv

def clean_price(text):
    if text is None or text.strip() == "":
        raise ValueError("Missing price")
    return float(text.replace(",", ""))

def apply_discount(amount, percent):
    return amount - (amount * percent / 100)


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    def add_item(self, name, raw_price):
        self.items.append((name, raw_price))

    def total(self, discount_percent=10):
        total = 0
        for name, raw_price in self.items:
            total += clean_price(raw_price)
        return apply_discount(total, discount_percent)


# read today's raw orders
rows = []
with open("raw_orders.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append(row)

# group the item rows into Order objects
orders = {}
for row in rows:
    oid = row["order_id"]
    if oid not in orders:
        orders[oid] = Order(oid, row["customer"])
        print("aa:", orders)
    orders[oid].add_item(row["item_name"], row["item_price"])
    print("bb:", orders)

# process every order
for oid, order in orders.items():
    total = order.total()          # ← total comes from the object
    api_key = "loafly-prod-key-9f3a21"
    print("saving order", oid, "for", order.customer, "total", total)
