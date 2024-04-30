# ./src/models/database_setup.py

import sqlite3
from configs.configs import DatabaseConfig

class Database:
    def __init__(self):
        self.conn = sqlite3.connect(f"{DatabaseConfig.DATABASE_PATH}/{DatabaseConfig.DATABASE_FILE}")
        self.cursor = self.conn.cursor()

    def create_tables(self):
        tables = [
            '''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                category TEXT,
                unit_price REAL NOT NULL,
                unit_cost REAL NOT NULL,
                sku TEXT NOT NULL
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                reorder_point INTEGER NOT NULL,
                reorder_quantity INTEGER NOT NULL,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (product_id) REFERENCES Products(id)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Suppliers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                contact TEXT
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS PurchaseOrders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                supplier_id INTEGER NOT NULL,
                order_date DATE NOT NULL,
                expected_delivery_date DATE,
                total_cost REAL NOT NULL,
                FOREIGN KEY (supplier_id) REFERENCES Suppliers(id)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS OrderItems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                purchase_order_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                unit_cost REAL NOT NULL,
                FOREIGN KEY (purchase_order_id) REFERENCES PurchaseOrders(id),
                FOREIGN KEY (product_id) REFERENCES Products(id)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                sale_date DATE NOT NULL,
                total_revenue REAL NOT NULL
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS SaleItems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sale_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                FOREIGN KEY (sale_id) REFERENCES Sales(id),
                FOREIGN KEY (product_id) REFERENCES Products(id)
            );
            ''',
            '''
            CREATE TABLE IF NOT EXISTS Customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT,
                contact TEXT
            );
            '''
        ]

        for table in tables:
            self.cursor.execute(table)

        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    db = Database()
    db.create_tables()
