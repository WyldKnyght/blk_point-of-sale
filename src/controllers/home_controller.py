from src.views.home_page import HomePage
from src.models.database import Database

class HomeController:
    def __init__(self, root):
        self.root = root
        self.home_page = HomePage(root)
        self.database = Database("database.db")

    def add_product_to_inventory(self, product, quantity, reorder_point, reorder_quantity):
        self.database.add_product_to_inventory(product, quantity, reorder_point, reorder_quantity)
        self.home_page.refresh_inventory()

    def get_inventory(self):
        return self.database.get_inventory()
