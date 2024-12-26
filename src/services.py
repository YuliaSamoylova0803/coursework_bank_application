import json
import re
from logging import getLogger
from pathlib import Path

from src.settings import BASE_DIR

logger = getLogger(__name__)

excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")


from src.utils import get_dict_transaction, logger


def search_transactions_for_individuals(dict_transaction: list[dict], pattern: str):
    """Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физическим лицам"""
    logger.info("Вызвана функция get_transactions_fizlicam")
    search_transactions_fizface = []
    for transaction in dict_transaction:
        if "Описание" in transaction and re.match(pattern, transaction["Описание"]):
            search_transactions_fizface.append(transaction)
    logger.info(f"Найдено {len(search_transactions_fizface)} транзакций, соответствующих паттерну")
    if search_transactions_fizface:
        search_transactions_fizface_json = json.dumps(search_transactions_fizface, ensure_ascii=False)
        logger.info(f"Возвращен JSON со {len(search_transactions_fizface)} транзакциями")
        return search_transactions_fizface_json
    else:
        logger.info("Возвращен пустой список")
        return []


if __name__ == "__main__":
    search_transactions_fizface_json = search_transactions_for_individuals(
        get_dict_transaction(excel_filename), pattern=r"\b[А-Я][а-я]+\s[А-Я]\."
    )
    print(search_transactions_fizface_json)
