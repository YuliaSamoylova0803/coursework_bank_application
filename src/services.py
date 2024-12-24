import json
import re

from src.utils import get_dict_transaction


# logger = logging.getLogger("logs")
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler("..\\logs\\services.log", encoding="utf-8")
# file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)

def search_transactions_for_individuals(dict_transaction: list[dict], pattern: str):
    """Функция возвращает JSON со всеми транзакциями, которые относятся к переводам физическим лицам"""
    #logger.info("Вызвана функция get_transactions_fizlicam")
    search_transactions_fizface = []
    for transaction in dict_transaction:
        if "Описание" in transaction and re.match(pattern, transaction["Описание"]):
            search_transactions_fizface.append(transaction)
    #logger.info(f"Найдено {len(list_transactions_fl)} транзакций, соответствующих паттерну")
    if search_transactions_fizface:
        search_transactions_fizface_json = json.dumps(search_transactions_fizface, ensure_ascii=False)
        #logger.info(f"Возвращен JSON со {len(list_transactions_fl)} транзакциями")
        return search_transactions_fizface_json
    else:
        #logger.info("Возвращен пустой список")
        return []



if __name__ == "__main__":
    search_transactions_fizface_json = search_transactions_for_individuals(
        get_dict_transaction("../data/operations.xlsx"), pattern=r"\b[А-Я][а-я]+\s[А-Я]\."
    )
    print(search_transactions_fizface_json)


