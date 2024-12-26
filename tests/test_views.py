from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from src.settings import BASE_DIR
from src.views import get_currency_exchange_rates, get_greeting, get_stock_prices

project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")


test_date = [
    ("2018-02-16 12:01:58", "Добрый день"),
    ("2018-02-16 10:01:58", "Доброе утро"),
    ("2018-02-16 18:01:58", "Добрый вечер"),
    ("2018-02-16 03:01:58", "Доброй ночи"),
    ("2018-02-16 23:01:58", "Доброй ночи"),
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
    mocked_get.return_value.status_code = 200
    mocked_response.json.return_value = []
    mocked_get.return_value = mocked_response
    result = get_currency_exchange_rates(stock_rates_path)
    assert result == [
        {"currency": "USD", "rate": 99.82},
        {"currency": "EUR", "rate": 103.83},
        {"currency": "AED", "rate": 27.18},
        {"currency": "CNY", "rate": 13.67},
        {"currency": "GBP", "rate": 125.25},
        {"currency": "CHF", "rate": 111.0},
        {"currency": "KZT", "rate": 0.19},
        {"currency": "BYN", "rate": 29.95},
    ]


@patch("json.load")
@patch("requests.get")
def test_get_stock_prices(mocked_get, mocked_json_load, stocks_price):
    mocked_response = Mock()
    mocked_json_load.return_value = {"user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}
    mocked_response.json.return_value = []
    mocked_get.return_value.status_code = 200
    mocked_get.return_value = mocked_response
    result = get_stock_prices(stock_rates_path)
    assert result == [
        {"stock": "AAPL", "price": 211.8},
        {"stock": "AMZN", "price": 188.8},
        {"stock": "GOOGL", "price": 168.5},
        {"stock": "MSFT", "price": 425.0},
        {"stock": "TSLA", "price": 233.7},
    ]
