from datetime import datetime
import datetime as dt



def get_date(date: str):
    """Функция преобразования даты"""
    #logger.info(f"Получена строка даты: {date}")
    date_update = datetime.strptime(date, "%d.%m.%Y")
    return date_update.strftime("%Y-%m-%d")

date_times = get_date("24.12.2024")
print(date_times)


