import logging
from .config import CONFIG

def clean_price(text):
    try:
        if text is None or text.strip() == "":
            raise ValueError("Missing price")
        return float(text.replace(",", ""))
    except Exception as e:
        logging.warning(f"Skipping item due to price error: {e}")
        return None
    finally:
        logging.debug("Finished price cleaning attempt")

def apply_discount(amount):
    percent = CONFIG["discount_percent"]
    return amount - (amount * percent / 100)
