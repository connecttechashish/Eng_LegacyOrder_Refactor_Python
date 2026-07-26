from .config import CONFIG

def clean_price(text):
    if text is None or text.strip() == "":
        raise ValueError("Missing price")
    return float(text.replace(",", ""))

def apply_discount(amount):
    percent = CONFIG["discount_percent"]
    return amount - (amount * percent / 100)
