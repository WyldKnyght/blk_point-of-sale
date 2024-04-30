# ./src/main.py

import tkinter as tk
from src.controllers.home_controller import HomeController
from ui_event_handlers.inventory_management import InventoryPage

def main():
    root = tk.Tk()
    home_controller = HomeController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
