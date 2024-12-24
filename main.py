import json
import logging
from pathlib import Path
from src.settings import BASE_DIR

import logging.config
from logging import getLogger, basicConfig, INFO, FileHandler, DEBUG, StreamHandler, ERROR

from src.utils import project_log

with open("logging.config") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()
FORMAT = "%(asctime)s - %(name)s - %(levelname)s: %(message)s"
file_handler = FileHandler(project_log)
file_handler.setLevel(DEBUG)
console = StreamHandler()
console.setLevel(ERROR)
basicConfig(level=INFO, format=FORMAT, handlers=[file_handler, console])


excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")
