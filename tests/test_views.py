import pytest
from datetime import datetime
from unittest.mock import Mock, patch
import json
from pathlib import Path
from src.settings import BASE_DIR
from src.views import get_greeting, get_currency_exchange_rates, get_stock_prices

project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")


test_date = [
    ("2018-02-16 12:01:58", "Добрый день"),
    ("2018-02-16 10:01:58", "Доброе утро"),
    ("2018-02-16 18:01:58", "Добрый вечер"),
    ("2018-02-16 03:01:58", "Доброй ночи"),
    ("2018-02-16 23:01:58", "Доброй ночи")
]


@pytest.mark.parametrize("date_now, expected_greeting", test_date)
def test_get_greeting(date_now, expected_greeting):
    """Тестирование функции вывода приветствия в зависимости от времени суток"""
    assert get_greeting(date_now) == expected_greeting


@patch("json.load")
@patch("requests.get")
def test_get_currency_exchange_rates(mocked_get, mocked_json_load, exchange_rates):
    mocked_response = Mock()
    mocked_json_load.return_value = {"user_currencies": ["USD", "EUR", "AED", "CNY", "GBP", "CHF", "KZT", "BYN"]}
    mocked_response.json.return_value = []
    mocked_get.return_value = mocked_response
    result = get_currency_exchange_rates(stock_rates_path)
    assert result == [
        {'currency': 'USD', 'rate': 100.1743},
        {'currency': 'EUR', 'rate': 104.1774},
        {'currency': 'AED', 'rate': 27.2769},
        {'currency': 'CNY', 'rate': 13.728},
        {'currency': 'GBP', 'rate': 125.6788},
        {'currency': 'CHF', 'rate': 111.3147},
        {'currency': 'KZT', 'rate': 0.1938},
        {'currency': 'BYN', 'rate': 29.8479}
    ]


@patch("json.load")
@patch("requests.get")
def test_get_stock_prices(mocked_get, mocked_json_load, stocks_price):
    mocked_response = Mock()
    mocked_json_load.return_value = {"user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}
    mocked_response.json.return_value = []
    mocked_get.return_value = mocked_response
    result = get_stock_prices(stock_rates_path)
    assert result == [
        {'stock': 'AAPL', 'price': 211.34505},
            {'stock': 'AMZN', 'price': 188.5215},
            {'stock': 'GOOGL', 'price': 168.1646},
            {'stock': 'MSFT', 'price': 424.77774},
            {'stock': 'TSLA', 'price': 232.245}
    ]



