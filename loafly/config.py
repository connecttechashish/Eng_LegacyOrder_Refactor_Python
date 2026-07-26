import os

CONFIG = {
    "currency": "USD",
    "discount_percent": 10,
    "input_file": "raw_orders.csv",
    "retry_count": 3,
    "retry_wait_seconds": 2,
    "log_file": "loafly.log",
    "api_key": os.getenv("LOAFLY_API_KEY")
}