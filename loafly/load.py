from .config import CONFIG

def save_order(order):
    retries = CONFIG["retry_count"]
    for attempt in range(1, retries + 1):
        try:
            print("saving order", order.order_id, "for", order.customer, "total", order.total())
            return
        except Exception as e:
            print("attempt", attempt, "failed:", e)
    print("giving up after", retries, "retries")
