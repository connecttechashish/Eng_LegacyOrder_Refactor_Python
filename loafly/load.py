import logging
from .config import CONFIG

def save_order(order):
    retries = CONFIG["retry_count"]
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Saving order {order.order_id} for {order.customer} total {order.total()}")
            return
        except Exception as e:
            logging.error(f"Attempt {attempt} failed: {e}")
    logging.error(f"Giving up after {retries} retries")
