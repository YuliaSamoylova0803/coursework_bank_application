from datetime import datetime




def get_greeting(date_now: datetime) -> str:
    """Функция выводит различное приветствие в зависимости от времени суток"""
    #greeting_by_time_of_day_logger.info('Начало работы функции вывода приветствия')
    hour = date_now.hour
    if 6 <= hour < 12:
        greeting = "Доброе утро"
    elif 12 <= hour < 18:
        greeting = "Добрый день"
    elif 18 <= hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"
    #greeting_by_time_of_day_logger.info('Функция возвращает приветствие в зависимости от времени')
    return greeting