import csv

def clean_price(text):
    """Convert price text like '1,234.50' into a float."""
    if text is None or text.strip() == "":
        raise ValueError("Missing price")
    return float(text.replace(",", ""))

def apply_discount(amount, percent):
    """Apply a percent discount to a numeric amount."""
    return amount - (amount * percent / 100)

# read today's raw orders
rows = []
with open("raw_orders.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        rows.append(row)

# group the item rows into orders
orders = {}
for row in rows:
    oid = row["order_id"]
    if oid not in orders:
        orders[oid] = {"customer": row["customer"], "items": []}
        print("aa: ", orders)
    orders[oid]["items"].append((row["item_name"], row["item_price"]))
    print("bb: ", orders)

# process every order
for oid, o in orders.items():
    total = 0
    for name, price in o["items"]:
        total += clean_price(price)          # ← now using the function
    total = apply_discount(total, 10)        # ← percent passed in
    api_key = "loafly-prod-key-9f3a21"
    print("saving order", oid, "for", o["customer"], "total", total)
