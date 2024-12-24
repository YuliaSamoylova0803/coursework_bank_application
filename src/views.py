from datetime import datetime
from pathlib import Path

from main import logger
from src.settings import BASE_DIR
from logging import getLogger


logger = getLogger(__name__)

project_log = Path(BASE_DIR, "logs", "logs_file.txt")



def get_greeting(date_now: datetime) -> str:
    """Функция выводит различное приветствие в зависимости от времени суток"""
   logger.info('Начало работы функции вывода приветствия')
    hour = date_now.hour
    if 6 <= hour < 12:
        greeting = "Доброе утро"
    elif 12 <= hour < 18:
        greeting = "Добрый день"
    elif 18 <= hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"
    logger.info('Функция возвращает приветствие в зависимости от времени')
    return greeting