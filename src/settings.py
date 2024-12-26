from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")
