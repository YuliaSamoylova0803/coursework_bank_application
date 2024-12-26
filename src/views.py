import json
import os
from datetime import datetime
from logging import getLogger
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

from src.settings import BASE_DIR

logger = getLogger(__name__)

project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")


def get_greeting(input_datetime: str) -> str:
    """Функция принимает строку с датой и возвращает требуемое приветствие"""
    date_update = datetime.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
    time = date_update.strftime("%H:%M:%S")

    if time > "05:00:00" and time <= "12:00:00":
        return "Доброе утро"
    if time > "12:00:00" and time <= "18:00:00":
        return "Добрый день"
    if time > "18:00:00" and time <= "23:00:00":
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_currency_exchange_rates(json_file: str) -> list[Any]:
    """Функция принимает на вход json-файл и возвращает список словарей с курсами требуемых валют.
    Курс валюты функция импортирует через API"""
    logger.info("Открытие файла JSON")
    with open(json_file, "r") as file:
        currencies_stocks_list = json.load(file)
        currency_rates_list_dicts = []

    for i in currencies_stocks_list.get("user_currencies"):
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{i}"
        payload = {}
        headers = {"apikey": API_KEY}

        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code

        if status_code != 200:
            logger.info(f"Запрос не был успешным. Возможная причина: {response.reason}")
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
        else:
            result = response.json()

            currency_rates_dict = {"currency": i, "rate": round(result.get("conversion_rates").get("RUB"), 2)}
            currency_rates_list_dicts.append(currency_rates_dict)

    return currency_rates_list_dicts


if __name__ == "__main__":
    currency_rates = get_currency_exchange_rates(stock_rates_path)
    print(currency_rates)


def get_stock_prices(json_file: str) -> list[Any]:
    """Функция принимает на вход json-файл и возвращает список словарей с курсами требуемых акций.
    Стоимости акций функция импортирует через API"""
    logger.info("Стоимости акций получены")
    with open(json_file, "r", encoding="utf-8") as file:

        currencies_stocks_list = json.load(file)
        stock_prices_list_dicts = []

    for i in currencies_stocks_list.get("user_stocks"):
        url = f"https://financialmodelingprep.com/api/v3/quote/{i}?apikey={API_KEY_STOCK}"
        payload = {}
        headers = {"apikey": API_KEY_STOCK}

        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code

        if status_code != 200:
            print(f"Запрос не был успешным. Возможная причина: {response.reason}")
        else:
            result = response.json()

            stock_prices_dict = {"stock": i, "price": round(result[0].get("priceAvg200"), 1)}
            stock_prices_list_dicts.append(stock_prices_dict)

    return stock_prices_list_dicts


# print(get_stock_prices(stock_rates_path))

if __name__ == "__main__":

    stock_price = get_stock_prices(stock_rates_path)

    print(stock_price)
