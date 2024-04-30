# ./src/views/home_page.py
from tkinter import *
import tkinter as tk
from tkinter import ttk
from configs.configs import AppConfig

class HomePage:
    def __init__(self, master):
        self.master = master

        # Header
        header_frame = tk.Frame(self.master, bg=AppConfig.HEADER_BG_COLOR)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text=AppConfig.BUSINESS_NAME, font=(AppConfig.FONT_FAMILY, AppConfig.FONT_SIZE)).pack(side="left")
        tk.Button(header_frame, text="Logout", command=self.master.destroy).pack(side="right")

        # Tabs
        tab_frame = tk.Frame(self.master)
        tab_frame.pack(fill="x")

        self.dashboard_tab = tk.Button(tab_frame, text="Dashboard", command=self.dashboard_page)
        self.dashboard_tab.pack(side="left", padx=AppConfig.TAB_SPACING)

        self.inventory_tab = tk.Button(tab_frame, text="Inventory Management", command=self.inventory_page)
        self.inventory_tab.pack(side="left", padx=AppConfig.TAB_SPACING)

        self.sales_tab = tk.Button(tab_frame, text="Sales Management", command=self.sales_page)
        self.sales_tab.pack(side="left", padx=AppConfig.TAB_SPACING)

        self.vendor_tab = tk.Button(tab_frame, text="Vendor Management", command=self.vendor_page)
        self.vendor_tab.pack(side="left", padx=AppConfig.TAB_SPACING)

        self.customer_tab = tk.Button(tab_frame, text="Customer Management", command=self.customer_page)
        self.customer_tab.pack(side="left", padx=AppConfig.TAB_SPACING)

        self.reports_tab = tk.Button(tab_frame, text="Reports", command=self.reports_page)
        self.reports_tab.pack(side="left", padx=AppConfig.TAB_SPACING)

        # Footer
        footer_frame = tk.Frame(self.master, bg=AppConfig.FOOTER_BG_COLOR)
        footer_frame.pack(fill="x")
        tk.Label(footer_frame, text=f"Copyright {AppConfig.COPYRIGHT_YEAR} {AppConfig.COPYRIGHT_TEXT}").pack(side="left")
