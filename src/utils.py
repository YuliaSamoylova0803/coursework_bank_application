from datetime import datetime
import datetime as dt
from typing import Any
import json
import os

import pandas as pd
from pathlib import Path
import requests



from src.settings import BASE_DIR
from logging import getLogger

#from src.views import date_now

logger = getLogger(__name__)


excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")



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


def top_transactions(df_transactions):
    """Функция вывода топ 5 транзакций по сумме платежа"""
    #logger.info("Начало работы функции top_transaction")
    top_transactions = df_transactions.sort_values(by="Сумма платежа", ascending=True).iloc[:5]
    #logger.info("Получен топ 5 транзакций по сумме платежа")
    result_top_transaction = top_transactions.to_dict(orient="records")
    top_transaction_list = []
    for transaction in result_top_transaction:
        top_transaction_list.append(
            {
                "date": str(
                    (datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S"))
                    .date()
                    .strftime("%d.%m.%Y")
                ).replace("-", "."),
                "amount": transaction["Сумма платежа"],
                "category": transaction["Категория"],
                "description": transaction["Описание"],
            }
        )
    #logger.info("Сформирован список топ 5 транзакций")
    return top_transaction_list


if __name__ == "__main__":
    top_transaction_list = top_transactions(get_excel_dataframe(excel_filename))
    print(top_transaction_list)


def get_expenses_cards(df_transactions) -> list[dict]:
    """Функция, возвращающая расходы по каждой карте"""
    #logger.info("Начало выполнения функции get_expenses_cards")

    cards_dict = (
        df_transactions.loc[df_transactions["Сумма платежа"] < 0]
        .groupby(by="Номер карты")
        .agg("Сумма платежа")
        .sum()
        .to_dict()
    )
    #logger.debug(f"Получен словарь расходов по картам: {cards_dict}")

    expenses_cards = []
    for card, expenses in cards_dict.items():
        expenses_cards.append(
            {"last_digits": card, "total spent": abs(expenses), "cashback": abs(round(expenses / 100, 2))}
        )
        #logger.info(f"Добавлен расход по карте {card}: {abs(expenses)}")

    #logger.info("Завершение выполнения функции get_expenses_cards")
    return expenses_cards


if __name__ == "__main__":
    result_expenses_cards = get_expenses_cards(get_excel_dataframe(excel_filename))
    print(result_expenses_cards)
