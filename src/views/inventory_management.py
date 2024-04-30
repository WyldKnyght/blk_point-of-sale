# ./src/views/inventory_management.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from configs.configs import DatabaseConfig
import sqlite3

class InventoryPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.inventory_tree = ttk.Treeview(self)
        self.inventory_tree["columns"] = ("Product", "Quantity", "Reorder Point", "Reorder Quantity")
        self.inventory_tree.column("#0", width=0, stretch=tk.NO)
        self.inventory_tree.column("Product", anchor=tk.W, width=200)
        self.inventory_tree.column("Quantity", anchor=tk.W, width=100)
        self.inventory_tree.column("Reorder Point", anchor=tk.W, width=100)
        self.inventory_tree.column("Reorder Quantity", anchor=tk.W, width=100)
        self.inventory_tree.heading("#0", text="", anchor=tk.W)
        self.inventory_tree.heading("Product", text="Product", anchor=tk.W)
        self.inventory_tree.heading("Quantity", text="Quantity", anchor=tk.W)
        self.inventory_tree.heading("Reorder Point", text="Reorder Point", anchor=tk.W)
        self.inventory_tree.heading("Reorder Quantity", text="Reorder Quantity", anchor=tk.W)

        self.inventory_tree.pack(fill=tk.BOTH, expand=1)

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_inventory)
        self.refresh_button.pack(fill=tk.X, padx=10, pady=10)

        self.add_button = ttk.Button(self, text="Add Product", command=self.add_product)
        self.add_button.pack(fill=tk.X, padx=10, pady=10)

        self.refresh_inventory()

    def refresh_inventory(self):
        self.inventory_tree.delete(*self.inventory_tree.get_children())
        conn = sqlite3.connect(f"{DatabaseConfig.DATABASE_PATH}/{DatabaseConfig.DATABASE_FILE}")
        cursor = conn.cursor()
        cursor.execute("SELECT p.name, i.quantity, i.reorder_point, i.reorder_quantity FROM Inventory i JOIN Products p ON i.product_id = p.id")
        rows = cursor.fetchall()
        for row in rows:
            self.inventory_tree.insert("", tk.END, values=row)
        conn.close()

    def add_product(self):
        # Create a new window to add a product
        add_window = tk.Toplevel(self)
        add_window.title("Add Product")

        # Create labels and entries for product information
        product_label = tk.Label(add_window, text="Product:")
        product_label.pack(fill=tk.X, padx=10, pady=10)
        product_entry = tk.Entry(add_window)
        product_entry.pack(fill=tk.X, padx=10, pady=10)

        quantity_label = tk.Label(add_window, text="Quantity:")
        quantity_label.pack(fill=tk.X, padx=10, pady=10)
        quantity_entry = tk.Entry(add_window)
        quantity_entry.pack(fill=tk.X, padx=10, pady=10)

        reorder_point_label = tk.Label(add_window, text="Reorder Point:")
        reorder_point_label.pack(fill=tk.X, padx=10, pady=10)
        reorder_point_entry = tk.Entry(add_window)
        reorder_point_entry.pack(fill=tk.X, padx=10, pady=10)

        reorder_quantity_label = tk.Label(add_window, text="Reorder Quantity:")
        reorder_quantity_label.pack(fill=tk.X, padx=10, pady=10)
        reorder_quantity_entry = tk.Entry(add_window)
        reorder_quantity_entry.pack(fill=tk.X, padx=10, pady=10)

        # Create a button to add the product
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_product_to_inventory(product_entry.get(), quantity_entry.get(), reorder_point_entry.get(), reorder_quantity_entry.get()))
        add_button.pack(fill=tk.X, padx=10, pady=10)

def add_product_to_inventory(self, product, quantity, reorder_point, reorder_quantity):
    try:
        quantity = int(quantity)
        reorder_point = int(reorder_point)
        reorder_quantity = int(reorder_quantity)
    except ValueError:
        messagebox.showerror("Error", "Quantity, reorder point, and reorder quantity must be numbers")
        return

    conn = sqlite3.connect(f"{DatabaseConfig.DATABASE_PATH}/{DatabaseConfig.DATABASE_FILE}")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Products WHERE name=?", (product,))
    product_id = cursor.fetchone()
    if product_id is None:
        cursor.execute("INSERT INTO Products (name) VALUES (?)", (product,))
        product_id = cursor.lastrowid
    else:
        product_id = product_id[0]
    cursor.execute("INSERT INTO Inventory (product_id, quantity, reorder_point, reorder_quantity) VALUES (?, ?, ?, ?)", (product_id, quantity, reorder_point, reorder_quantity))
    conn.commit()
    conn.close()
    self.refresh_inventory()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Inventory Management System")
    app = InventoryPage(root, None)
    app.pack(fill=tk.BOTH, expand=1)
    root.mainloop()
