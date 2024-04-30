# ./src/configs/configs.py
import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    BUSINESS_NAME = os.getenv('BUS_NAME')
    FONT_FAMILY = "Arial"
    FONT_SIZE = 18
    COPYRIGHT_YEAR = 2024
    COPYRIGHT_TEXT = os.getenv('BUS_NAME')
    TAB_SPACING = 5
    HEADER_BG_COLOR = "gray"
    FOOTER_BG_COLOR = "gray"

class DatabaseConfig:
    DATABASE_PATH = os.getenv('DB_PATH')
    DATABASE_FILE = os.getenv('DB_FILENAME')
