import csv
from .config import CONFIG

def extract_orders():
    path = CONFIG["input_file"]
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows
