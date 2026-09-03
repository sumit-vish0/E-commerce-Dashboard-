import sqlite3
from pathlib import Path
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_project.settings")
django.setup()

from inventory.models import Product

db = Path(__file__).resolve().parent / "ecommerce.db"
conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row

rows = conn.execute(
    "SELECT id, name, category, price, quantity, supplier, added_date FROM products ORDER BY id"
).fetchall()
conn.close()

existing_ids = set(Product.objects.values_list("id", flat=True))
products = [
    Product(
        id=row["id"],
        name=row["name"],
        category=row["category"],
        price=row["price"],
        quantity=row["quantity"],
        supplier=row["supplier"],
        added_date=row["added_date"],
    )
    for row in rows
    if row["id"] not in existing_ids
]

if products:
    Product.objects.bulk_create(products)
    print(f"Imported {len(products)} legacy products.")
else:
    print("No new legacy products to import.")
