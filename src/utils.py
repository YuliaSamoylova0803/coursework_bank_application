import datetime as dt
import json
import os
from datetime import datetime
from logging import getLogger
from pathlib import Path
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv

from src.settings import BASE_DIR

logger = getLogger(__name__)


excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")


load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")

date = "27.07.2019 19:08:23"


def get_date(date: str):
    """Функция преобразования даты"""
    logger.info(f"Получена строка даты: {date}")
    try:
        date_times = datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
        logger.info(f"Преобразована в объект datetime: {date_times}")
        return date_times
    except ValueError as e:
        logger.error(f"Ошибка преобразования даты: {e}")
        raise e


# if __name__ == "__main__":
#     date_times = get_date("29.07.2019 22:06:27")
#     print(date_times)


def get_excel_dataframe(path_excel: str) -> pd.DataFrame:
    """Функция для считывания финансовых операций из Excel и возвращает датафрейм"""
    logger.info(f"Вызвана функция получения транзакций из файла {path_excel}")
    try:
        df_transactions = pd.read_excel(path_excel)
        logger.info(f"Файл {path_excel} найден, данные о транзакциях получены")
        return df_transactions

    except FileNotFoundError:
        logger.info(f"Файл {path_excel} не найден")
        raise


# if __name__ == "__main__":
#     df_transactions = get_excel_dataframe(excel_filename)
#     print(df_transactions)
#     print(type(df_transactions))


def get_dict_transaction(path_excel) -> list[dict]:
    """Функция преобразовывающая датафрейм в словарь pyhton"""
    logger.info(f"Вызвана функция get_dict_transaction с файлом {path_excel}")
    try:
        df = pd.read_excel(path_excel)
        logger.info(f"Файл {path_excel}  прочитан")
        dict_transaction = df.to_dict(orient="records")
        logger.info("Датафрейм преобразован в список словарей")
        return dict_transaction
    except FileNotFoundError:
        logger.error(f"Файл {path_excel} не найден")
        raise
    except Exception as e:
        logger.error(f"Произошла ошибка: {str(e)}")
        raise


# if __name__ == "__main__":
#     dict_transaction = get_dict_transaction((excel_filename))
#
#     print(get_dict_transaction(excel_filename))
#     print(type(dict_transaction))
#     #print(type(df))
#     #print(dict_transaction)


def top_transactions(df_transactions):
    """Функция вывода топ 5 транзакций по сумме платежа"""
    logger.info("Начало работы функции top_transaction")
    top_transactions = df_transactions.sort_values(by="Сумма платежа", ascending=True).iloc[:5]
    logger.info("Получен топ 5 транзакций по сумме платежа")
    result_top_transaction = top_transactions.to_dict(orient="records")
    top_transaction_list = []
    for transaction in result_top_transaction:
        top_transaction_list.append(
            {
                "date": str(
                    (datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S")).date().strftime("%d.%m.%Y")
                ).replace("-", "."),
                "amount": transaction["Сумма платежа"],
                "category": transaction["Категория"],
                "description": transaction["Описание"],
            }
        )
    # logger.info("Сформирован список топ 5 транзакций")
    return top_transaction_list


# if __name__ == "__main__":
#     top_transaction_list = top_transactions(get_excel_dataframe(excel_filename))
#     print(top_transaction_list)


def get_expenses_cards(df_transactions) -> list[dict]:
    """Функция, возвращающая расходы по каждой карте"""
    logger.info("Начало выполнения функции get_expenses_cards")

    cards_dict = (
        df_transactions.loc[df_transactions["Сумма платежа"] < 0]
        .groupby(by="Номер карты")
        .agg("Сумма платежа")
        .sum()
        .to_dict()
    )
    logger.debug(f"Получен словарь расходов по картам: {cards_dict}")

    expenses_cards = []
    for card, expenses in cards_dict.items():
        expenses_cards.append(
            {"last_digits": card, "total spent": abs(expenses), "cashback": abs(round(expenses / 100, 2))}
        )
        logger.info(f"Добавлен расход по карте {card}: {abs(expenses)}")

    logger.info("Завершение выполнения функции get_expenses_cards")
    return expenses_cards


# if __name__ == "__main__":
#     result_expenses_cards = get_expenses_cards(get_excel_dataframe(excel_filename))
#     print(result_expenses_cards)


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
#
# if __name__ == "__main__":
#
#     stock_price = get_stock_prices(stock_rates_path)
#
#     print(stock_price)


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


# if __name__ == "__main__":
#     currency_rates = get_currency_exchange_rates(stock_rates_path)
#     print(currency_rates)


def get_greeting():
    """Функция- приветствие"""
    hour = dt.datetime.now().hour
    if 4 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 17 <= hour < 22:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


# if __name__ == "__main__":
#
#     date_times = get_date(date)
#     greeting = get_greeting()
#     print(greeting)
#     #greeting = get_greeting(get_date(date))
