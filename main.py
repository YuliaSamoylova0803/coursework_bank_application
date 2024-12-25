import json
import logging
from pathlib import Path
from src.settings import BASE_DIR
import pandas as pd

import logging.config
from logging import getLogger, basicConfig, INFO, FileHandler, DEBUG, StreamHandler, ERROR

from src.utils import get_excel_dataframe, top_transactions, get_expenses_cards
from src.views import get_greeting, get_currency_exchange_rates, get_stock_prices



excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")

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


# Входящая дата
date_now = "2018-02-16 12:01:58"

def main():
    """Функция принимает на вход DataFrame и возвращает json-файл"""
    logger.info('Начало работы функции main')
    greeting = get_greeting(date_now)
    cards = get_expenses_cards(get_excel_dataframe(excel_filename))
    top_trans = top_transactions(get_excel_dataframe(excel_filename))
    stocks_prices = get_stock_prices(stock_rates_path)
    currency_rates = get_currency_exchange_rates(stock_rates_path)
    logger.info('Формирование JSON ответа')
    result_list_dicts = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_trans,
        "currency_rates": currency_rates,
        "stock_prices": stocks_prices,
    }

    # Формируем json-ответ
    logger.info("json-ответ создан успешно")
    json_output = json.dumps(result_list_dicts, ensure_ascii=False, indent=4)
    return json_output


if __name__ == "__main__":
    print(main())