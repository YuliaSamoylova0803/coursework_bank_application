from datetime import datetime
import datetime as dt
from typing import Any
import json
import os

import pandas as pd
from pathlib import Path
import requests
from dotenv import load_dotenv

from main import logger
from src.settings import BASE_DIR
from logging import getLogger


logger = getLogger(__nam__)


excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_STOCK = os.getenv("API_KEY_STOCK")


def get_date(date: str):
    """Функция преобразования даты"""
    logger.info(f"Получена строка даты: {date}")
    date_update = datetime.strptime(date, "%d.%m.%Y")
    return date_update.strftime("%Y-%m-%d")

date_times = get_date("24.12.2024")
print(date_times)


def first_month_day(input_datetime: str) -> dt:
    """Функция принимает на вход строку с датой и возвращает начало месяца"""
    logger.info(f"Вызвана функция получения начала месяца")
    date_update = datetime.strptime(input_datetime, "%Y-%m-%d %H:%M:%S")
    start_day = date_update.replace(day=1, hour=0, minute=0, second=0)
    return start_day


#begin_month = first_month_day(input_datetime)


def get_excel_dataframe(path_excel: str) -> pd.DataFrame:
    """Функция для считывания финансовых операций из Excel и возвращает датафрейм"""
    logger.info(f"Вызвана функция получения транзакций из файла {file_path}")
    try:
        df_transactions = pd.read_excel(path_excel)
        logger.info(f"Файл {path_excel} найден, данные о транзакциях получены")
        return df_transactions

    except FileNotFoundError:
        logger.info(f"Файл {path_excel} не найден")
        raise


print(get_excel_dataframe(excel_filename))


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

print(get_dict_transaction(excel_filename)[0])


def get_currency_exchange_rates(json_file: str) -> list[Any]:
    """Функция принимает на вход json-файл и возвращает список словарей с курсами требуемых валют.
     Курс валюты функция импортирует через API"""
    logger.info("Открытие файла JSON")
    with open(json_file, "r", encoding="utf-8") as file:
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

            currency_rates_dict = {"currency": i, "rate": result.get("conversion_rates").get("RUB")}
            currency_rates_list_dicts.append(currency_rates_dict)

    return currency_rates_list_dicts


# if __name__ == "__main__":
#     currency_rates = get_currency_exchange_rates(rel_src_file_path1)
#     print(currency_rates)


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

            stock_prices_dict = {"stock": i, "price": result[0].get("priceAvg200")}
            stock_prices_list_dicts.append(stock_prices_dict)

    return stock_prices_list_dicts


#print(get_stock_prices("user_settings.json"))

# if __name__ == "__main__":
#     #print(get_currency_exchange_rates(["USD", "EUR", "JPY"]))
#
#     stock = "AAPL"
#     stock_price = get_stock_prices(rel_src_file_path1)
#
#     print(stock_price)


def filter_date(df_test: str) -> pd.DataFrame:
    """Функция создает DataFrame по заданному периоду времени"""
    logger.info("Функция начала сортировать")
    df = pd.read_excel(df_test)
    df_date = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filtered_df_to_date = df[(begin_month <= df_date) & (df_date <= input_datetime)]
    return filtered_df_to_date


filtered_df_to_date = filter_date(excel_filename)


def cards_info(df_transactions: pd.DataFrame) -> list[dict[str, Any]]:
    """Функция, возвращающая расходы по каждой карте"""

    df_input = df_transactions
    df_output = []
    try:
        logger.info("Данные из файла xlsx импортированы")

        cards = df_input.groupby("Номер карты")
        cards_prices = cards["Сумма операции с округлением"].sum()
        df_test = cards_prices.to_dict()

        for cards, sum in df_test.items():
            df_result = {}
            df_result["last_digits"] = cards
            df_result["total_spent"] = sum
            df_result["cashback"] = round(sum / 100, 2)
            df_output.append(df_result)
        return df_output
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return [{}]


def top_transactions(df_transactions: pd.DataFrame) -> list[dict[str, Any]] | None:
    """Функция принимает на вход DataFrame и возвращает ТОП-5 транзакций по сумме платежа"""
    df_transactions = get_excel_dataframe(excel_filename)
    df_input_sort = df_transactions
    df_output_sort = []
    try:
        logger.info("Данные из файла xlsx импортированы")

        sorted_df = df_input_sort.sort_values("Сумма платежа", ascending=False)
        sort_five = sorted_df.iloc[0:5]

        df_sort_dict = sort_five.to_dict("records")
        for i in df_sort_dict:
            df_sort_result = {}
            df_sort_result["date"] = i["Дата платежа"]
            df_sort_result["amount"] = i["Сумма платежа"]
            df_sort_result["category"] = i["Категория"]
            df_sort_result["description"] = i["Описание"]
            df_output_sort.append(df_sort_result)
        return df_output_sort
    except Exception:
        logger.warning("Импортируемый список пуст или отсутствует.")
        return None
