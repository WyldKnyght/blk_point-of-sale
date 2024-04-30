# ./src/views/gui_inventory.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class InventoryGUI(tk.Frame):
    def __init__(self, parent, refresh_callback, add_product_callback):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.refresh_callback = refresh_callback
        self.add_product_callback = add_product_callback
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

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_callback)
        self.refresh_button.pack(fill=tk.X, padx=10, pady=10)

        self.add_button = ttk.Button(self, text="Add Product", command=self.add_product_callback)
        self.add_button.pack(fill=tk.X, padx=10, pady=10)