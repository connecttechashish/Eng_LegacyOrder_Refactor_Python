from loafly.extract import extract_orders
from loafly.models import Order
from loafly.load import save_order
from loafly.config import API_KEY

def run():
    rows = extract_orders()

    orders = {}
    for row in rows:
        oid = row["order_id"]
        if oid not in orders:
            orders[oid] = Order(oid, row["customer"])
        orders[oid].add_item(row["item_name"], row["item_price"])

    for order in orders.values():
        save_order(order, API_KEY)

if __name__ == "__main__":
    run()
