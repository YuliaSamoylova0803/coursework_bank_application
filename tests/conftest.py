import pandas as pd
import pytest


@pytest.fixture
def exchange_rates():
    return [
        {"currency": "USD", "rate": 103.32},
        {"currency": "EUR", "rate": 107.75},
        {"currency": "AED", "rate": 28.13},
        {"currency": "CNY", "rate": 14.16},
        {"currency": "GBP", "rate": 129.84},
        {"currency": "CHF", "rate": 114.66},
        {"currency": "KZT", "rate": 0.2},
        {"currency": "BYN", "rate": 31.65},
    ]


@pytest.fixture
def currencies_stocks_list():
    return ["USD", "EUR", "AED", "CNY", "GBP", "CHF", "KZT", "BYN"]


@pytest.fixture
def stocks_price():
    return [
        {"stock": "AAPL", "price": 213.4},
        {"stock": "AMZN", "price": 189.7},
        {"stock": "GOOGL", "price": 169.5},
        {"stock": "MSFT", "price": 425.2},
        {"stock": "TSLA", "price": 238.8},
    ]


@pytest.fixture
def mocked_file():
    return "path/to/open"


@pytest.fixture
def data_for_tests():
    # Пример тестовых данных
    data = {
        "Дата операции": [
            "01.01.2021 12:00:00",
            "15.12.2021 10:30:00",
            "25.12.2021 18:45:00",
            "05.01.2022 08:00:00",
            "20.02.2022 16:20:00",
        ],
        "Категория": ["Продукты", "Продукты", "Транспорт", "Продукты", "Транспорт"],
        "Сумма": [100, 200, 50, 150, 80],
    }
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def df_transaction_1():
    # Пример тестовых данных
    data = {
        "Дата операции": [
            "31.12.2021 12:00:00",
            "15.12.2021 10:30:00",
            "25.11.2021 18:45:00",
            "05.10.2022 08:00:00",
            "20.10.2022 16:20:00",
        ],
        "Категория": ["Медицина", "Продукты", "Медицина", "Продукты", "Медицина"],
        "Сумма": [5000, 200, 15000, 150, 3000],
    }
    df = pd.DataFrame(data)
    return df


@pytest.fixture
def sample_transactions():
    return pd.DataFrame({"Номер карты": ["*7197", "*4556", "*5091"], "Сумма платежа": [-100, -100, -100]})


@pytest.fixture
def top_trans_data():
    """Создает фиктивные данные для тестирования."""
    data_top = [
        {
            "Дата операции": "31.12.2021 16:44:00",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -160.89,
            "Валюта операции": "RUB",
            "Сумма платежа": -160.89,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 3,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 160.89,
        },
        {
            "Дата операции": "31.12.2021 16:42:04",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -64.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -64.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 64.0,
        },
        {
            "Дата операции": "31.12.2021 16:39:04",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -118.12,
            "Валюта операции": "RUB",
            "Сумма платежа": -118.12,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Магнит",
            "Бонусы (включая кэшбэк)": 2,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 118.12,
        },
        {
            "Дата операции": "31.12.2021 15:44:39",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -78.05,
            "Валюта операции": "RUB",
            "Сумма платежа": -78.05,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Супермаркеты",
            "MCC": 5411.0,
            "Описание": "Колхоз",
            "Бонусы (включая кэшбэк)": 1,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 78.05,
        },
        {
            "Дата операции": "31.12.2021 01:23:42",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*5091",
            "Статус": "OK",
            "Сумма операции": -564.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -564.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Различные товары",
            "MCC": 5399.0,
            "Описание": "Ozon.ru",
            "Бонусы (включая кэшбэк)": 5,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 564.0,
        },
        {
            "Дата операции": "31.12.2021 00:12:53",
            "Дата платежа": "31.12.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -800.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -800.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Переводы",
            "MCC": None,
            "Описание": "Константин Л.",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 800.0,
        },
        {
            "Дата операции": "30.12.2021 22:22:03",
            "Дата платежа": "31.12.2021",
            "Номер карты": None,
            "Статус": "OK",
            "Сумма операции": -20000.0,
            "Валюта операции": "RUB",
            "Сумма платежа": -20000.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Переводы",
            "MCC": None,
            "Описание": "Константин Л.",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 20000.0,
        },
        {
            "Дата операции": "30.12.2021 19:18:22",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*5091",
            "Статус": "OK",
            "Сумма операции": -7.07,
            "Валюта операции": "RUB",
            "Сумма платежа": -7.07,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Каршеринг",
            "MCC": 7512.0,
            "Описание": "Ситидрайв",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 7.07,
        },
        {
            "Дата операции": "30.12.2021 19:06:39",
            "Дата платежа": "31.12.2021",
            "Номер карты": "*7197",
            "Статус": "OK",
            "Сумма операции": -1.32,
            "Валюта операции": "RUB",
            "Сумма платежа": -1.32,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Каршеринг",
            "MCC": 7512.0,
            "Описание": "Ситидрайв",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 1.32,
        },
        {
            "Дата операции": "30.12.2021 17:50:30",
            "Дата платежа": "30.12.2021",
            "Номер карты": "*4556",
            "Статус": "OK",
            "Сумма операции": 5046.0,
            "Валюта операции": "RUB",
            "Сумма платежа": 5046.0,
            "Валюта платежа": "RUB",
            "Кэшбэк": None,
            "Категория": "Пополнения",
            "MCC": None,
            "Описание": "Пополнение через Газпромбанк",
            "Бонусы (включая кэшбэк)": 0,
            "Округление на инвесткопилку": 0,
            "Сумма операции с округлением": 5046.0,
        },
    ]
    df = pd.DataFrame(data_top)

    return df


@pytest.fixture
def sample_dict_transaction():
    return [
        {"Описание": "Константин Л."},
        {"Описание": "Оплата услуг"},
    ]
