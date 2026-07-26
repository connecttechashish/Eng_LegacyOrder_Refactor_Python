import logging
import time
from .config import CONFIG
from .gateway import save_to_orders_api

def save_order(order):
    api_key = CONFIG["api_key"]
    if not api_key:
        logging.error("Missing LOAFLY_API_KEY in environment")
        return

    retries = CONFIG["retry_count"]
    wait = CONFIG["retry_wait_seconds"]

    for attempt in range(1, retries + 1):
        try:
            result = save_to_orders_api(order.order_id, order.total())
            logging.info(f"Saved order {order.order_id}: {result}")
            return
        except ConnectionError as e:
            logging.warning(f"Attempt {attempt} failed for order {order.order_id}: {e}")
            if attempt < retries:
                time.sleep(wait)
        except Exception as e:
            logging.error(f"Unexpected error for order {order.order_id}: {e}")
            return

    logging.error(f"Giving up after {retries} failed attempts for order {order.order_id}")
