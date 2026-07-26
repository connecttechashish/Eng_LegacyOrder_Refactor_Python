from loafly.extract import extract_orders
from loafly.models import Order
from loafly.load import save_order
from loafly.logging_setup import setup_logging

def run():
    setup_logging()

    from loafly.config import CONFIG
    import logging

    logging.info("Starting Loafly pipeline")

    rows = extract_orders()

    orders = {}
    for row in rows:
        oid = row["order_id"]
        if oid not in orders:
            orders[oid] = Order(oid, row["customer"])
            logging.info(f"Created order {oid}")
        orders[oid].add_item(row["item_name"], row["item_price"])

    for order in orders.values():
        save_order(order)

    logging.info("Pipeline completed")

if __name__ == "__main__":
    run()
