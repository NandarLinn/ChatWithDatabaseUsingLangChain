from dotenv import load_dotenv

load_dotenv()

import csv
import sys

from db import SessionLocal
from dateutil.parser import parse
from models import Orders, Products


csv_header_to_column_mapping = {
    "Order ID": "order_id",
    "Product": "product_name",
    "Quantity Ordered": "quantity_ordered",
    "Price Each": "price_each",
    "Order Date": "order_date",
    "Purchase Address": "purchase_address"
}


def read_sale_data(path: str):
    db = SessionLocal()
    mapper = lambda x: {csv_header_to_column_mapping.get(k): v for k, v in x.items()}
    with open(path) as file_sales_data:
        reader = csv.DictReader(file_sales_data)
        for row in reader:
            
            current_row = mapper(row)
            # print(current_row)

            if not all(current_row.values()):
                continue

            product_data = {
                "product_name": current_row["product_name"],
            }
            products = Products(**product_data)
            found_product = (
                db.query(Products)
                .filter_by(
                    product_name=product_data.get("product_name"),
                )
                .first()
            )
            if not found_product:
                db.add(products)
                db.commit()
                db.refresh(products)
                found_product = products

            orders_data = {
                "order_id": current_row["order_id"],
                "product_id": found_product.id,
                "quantity_ordered": current_row["quantity_ordered"],
                "price_each": current_row["price_each"],
                "order_date": parse(current_row["order_date"]),
                "purchase_address": current_row["purchase_address"],
            }
            # print(orders_data)

            orders = Orders(**orders_data)
            found_orders = (
                db.query(Orders)
                .filter_by(
                    order_id=orders_data.get("order_id"),
                    product_id=orders_data.get("product_id"),
                )
                .first()
            )
            if not found_orders:
                db.add(orders)
                db.commit()
                db.refresh(orders)


if __name__ == "__main__":
    # how to import data
    # cd /Users/linnaein/Projects/Testwork
    # source ../testwork_env/bin/activate
    # python -m seeds.importer ~/Downloads/sales_data\ -\ sales_data.csv
    read_sale_data(sys.argv[1])
