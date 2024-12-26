import datetime
import datetime as dt
from functools import wraps
from logging import getLogger
from pathlib import Path
from typing import Any, Callable, Optional

import pandas as pd

from src.settings import BASE_DIR
from src.utils import get_date, get_excel_dataframe

logger = getLogger(__name__)
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
excel_filename = Path(BASE_DIR, "data", "operations.xlsx")


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который может записать работу функции и ее результат как в файл, так и в консоль."""

    def logging_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return logging_decorator


@log(reports_log)
def spending_by_category(df_transactions, category: str, date: [str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)"""
    if date is None:
        fin_date = dt.datetime.now()
    else:
        fin_date = get_date(date)
    start_date = fin_date.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=91)
    transactions_by_category = df_transactions.loc[
        (pd.to_datetime(df_transactions["Дата операции"], dayfirst=True) <= fin_date)
        & (pd.to_datetime(df_transactions["Дата операции"], dayfirst=True) >= start_date)
        & (df_transactions["Категория"] == category)
    ]
    return transactions_by_category


if __name__ == "__main__":
    transactions_by_category = spending_by_category(
        get_excel_dataframe(excel_filename), "Медицина", "31.12.2021 12:00:00"
    )
    print(len(transactions_by_category))
