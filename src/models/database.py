# ./src/models/database.py

import sqlite3
from configs.configs import DatabaseConfig

db_path = f"{DatabaseConfig.DATABASE_PATH}/{DatabaseConfig.DATABASE_FILE}"

class Database:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        # create tables for inventory, sales, vendors, customers, reports
        pass

    def add_product_to_inventory(self, product, quantity, reorder_point, reorder_quantity):
        # add product to inventory table
        pass

    def get_inventory(self):
        # retrieve inventory data
        pass

    def close(self):
        self.conn.close()

