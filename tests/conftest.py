import pytest
import pandas as pd

@pytest.fixture
def exchange_rates():
    return [
        {'currency': 'USD', 'rate': 99.82},
        {'currency': 'EUR', 'rate': 103.83},
        {'currency': 'AED', 'rate': 27.18},
        {'currency': 'CNY', 'rate': 13.67},
        {'currency': 'GBP', 'rate': 125.25},
        {'currency': 'CHF', 'rate': 111.0},
        {'currency': 'KZT', 'rate': 0.19},
        {'currency': 'BYN', 'rate': 29.95}
    ]


@pytest.fixture
def stocks_price():
    return [
        {'stock': 'AAPL', 'price': 211.34505},
            {'stock': 'AMZN', 'price': 188.5215},
            {'stock': 'GOOGL', 'price': 168.1646},
            {'stock': 'MSFT', 'price': 424.77774},
            {'stock': 'TSLA', 'price': 232.245}
    ]


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