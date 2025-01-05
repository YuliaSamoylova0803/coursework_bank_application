import datetime
import datetime as dt
import unittest
from pathlib import Path
from unittest.mock import Mock, mock_open, patch

import pandas as pd
import pytest

from src.settings import BASE_DIR
from src.utils import (get_currency_exchange_rates, get_date, get_dict_transaction, get_excel_dataframe,
                       get_expenses_cards, get_greeting, get_stock_prices, get_user_setting, top_transactions)

excel_filename = Path(BASE_DIR, "data", "operations.xlsx")
reports_log = Path(BASE_DIR, "logs", "reports_file.txt")
project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")


@pytest.mark.parametrize(
    "date, formatted_date",
    [
        ("16.02.2018 12:00:00", datetime.datetime(2018, 2, 16, 12, 0)),
        ("01.01.2001 16:00:00", datetime.datetime(2001, 1, 1, 16, 0)),
        ("1.02.2018 19:00:00", datetime.datetime(2018, 2, 1, 19, 0)),
    ],
)
def test_get_date(date: str, formatted_date: str) -> str:
    """Функция тестирует вывод приветствия в зависимрсти от времени суток"""
    assert get_date(date) == formatted_date


def test_get_date_input():
    """Проверяем, что функция корректно обрабатывает ввод"""
    input_data = "26.12.2024 11:00:00"
    expected_output = datetime.datetime(2024, 12, 26, 11, 0, 0)
    assert get_date(input_data) == expected_output


def test_get_date_format_er():
    """Проверяем, что функция обрабатывает исключение при неверном формате ввода"""
    input_data = "01-01-2023 12:00:00"
    with pytest.raises(ValueError):
        get_date(input_data)


def test_get_date_empty_str_input():
    """Проверяем, что функция обрабатывает пустой ввод"""
    input_data = ""
    with pytest.raises(ValueError):
        get_date(input_data)


def test_get_excel_dataframe_file_not_found():
    """Проверка, что функция поднимает исключение при передаче несуществующего файла"""
    with pytest.raises(FileNotFoundError):
        get_excel_dataframe("path/to/non-existent/file.xlsx")


class TestReaderTransactionExcel(unittest.TestCase):
    @patch("pandas.read_excel")
    def test_successful_read(self, mock_read_excel):
        # Arrange
        mock_df = pd.DataFrame({"transaction_id": [1, 2, 3]})
        mock_read_excel.return_value = mock_df

        result = get_excel_dataframe("test_file.xlsx")

        self.assertEqual(result.shape, mock_df.shape)
        self.assertTrue(all(result["transaction_id"] == mock_df["transaction_id"]))


def test_get_dict_transaction_file_not_found():
    """Тест проверяет обработку ошибки FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        get_dict_transaction("non_existent_file.xlsx")


def test_get_expenses_cards(sample_transactions):
    result = get_expenses_cards(sample_transactions)

    assert result[0] == {"last_digits": "*4556", "total spent": 100, "cashback": 1.0}
    assert result[1] == {"last_digits": "*5091", "total spent": 100, "cashback": 1.0}
    assert result[2] == {"last_digits": "*7197", "total spent": 100, "cashback": 1.0}


def test_top_transactions(top_trans_data):
    assert top_transactions(top_trans_data) == [
        {"amount": -20000.0, "category": "Переводы", "date": "30.12.2021", "description": "Константин Л."},
        {"amount": -800.0, "category": "Переводы", "date": "31.12.2021", "description": "Константин Л."},
        {"amount": -564.0, "category": "Различные товары", "date": "31.12.2021", "description": "Ozon.ru"},
        {"amount": -160.89, "category": "Супермаркеты", "date": "31.12.2021", "description": "Колхоз"},
        {"amount": -118.12, "category": "Супермаркеты", "date": "31.12.2021", "description": "Магнит"},
    ]


def test_top_transactions_len(top_trans_data):
    assert len(top_transactions(top_trans_data)) == 5


def test_top_transaction_empty_list():
    """Тест на случай, если передан пустой список транзакций."""
    with pytest.raises(TypeError):
        top_transactions()


# @patch("json.load")
# @patch("requests.get")
# def test_get_currency_exchange_rates(mocked_get, mocked_json_load, exchange_rates):
#     mocked_response = Mock()
#     mocked_json_load.return_value = {"user_currencies": ["USD", "EUR", "AED", "CNY", "GBP", "CHF", "KZT", "BYN"]}
#     mocked_get.return_value.status_code = 200
#     mocked_response.json.return_value = []
#     mocked_get.return_value = mocked_response
#     result = get_currency_exchange_rates(stock_rates_path)
#     assert result == [
#         {"currency": "USD", "rate": 103.29},
#         {"currency": "EUR", "rate": 107.78},
#         {"currency": "AED", "rate": 28.12},
#         {"currency": "CNY", "rate": 14.16},
#         {"currency": "GBP", "rate": 129.83},
#         {"currency": "CHF", "rate": 114.71},
#         {"currency": "KZT", "rate": 0.2},
#         {"currency": "BYN", "rate": 31.55},
#     ]
#
#
# @patch("json.load")
# @patch("requests.get")
# def test_get_stock_prices(mocked_get, mocked_json_load, stocks_price):
#     mocked_response = Mock()
#     mocked_json_load.return_value = {"user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}
#     mocked_response.json.return_value = []
#     mocked_get.return_value.status_code = 200
#     mocked_get.return_value = mocked_response
#     result = get_stock_prices(stock_rates_path)
#     assert result == [
#         {"stock": "AAPL", "price": 212.2},
#         {"stock": "AMZN", "price": 189.1},
#         {"stock": "GOOGL", "price": 169.0},
#         {"stock": "MSFT", "price": 425.1},
#         {"stock": "TSLA", "price": 235.1},
#     ]


def test_get_greeting_morning():
    with pytest.raises(TypeError):
        with patch("datetime.datetime.now") as mock_now:
            mock_now.return_value = dt.datetime(2023, 4, 1, 8, 0, 0)
            assert get_greeting() == "Доброе утро"


def test_get_greeting_afternoon():
    with pytest.raises(TypeError):
        with patch("datetime.datetime.now") as mock_now:
            mock_now.return_value = dt.datetime(2023, 4, 1, 14, 0, 0)
            assert get_greeting() == "Добрый день"


def test_get_greeting_evening():
    with pytest.raises(TypeError):
        with patch("datetime.datetime.now") as mock_now:
            mock_now.return_value = dt.datetime(2023, 4, 1, 19, 0, 0)
            assert get_greeting() == "Добрый вечер"


def test_get_greeting_night():
    with pytest.raises(TypeError):
        with patch("datetime.datetime.now") as mock_now:
            mock_now.return_value = dt.datetime(2023, 4, 1, 23, 0, 0)
            assert get_greeting() == "Доброй ночи"


# #@patch("requests.request")
# @patch("builtins.open", new_callable=mock_open, read_data="user_stocks")
# def test_get_stock_prices(mocked_file):
#     with patch('builtins.open', mock_open(read_data="mocked currencies_stocks_list")) as mocked_file:
#         currencies_stocks_list = mocked_file.return_value.read()
#     get_stock_prices("path/to/open") == "mocked currencies_stocks_list"
#
#
# class TestGetStockPrices(unittest.TestCase):
#     @patch("requests.request")
#     @patch(
#         "builtins.open",
#         mock_open(
#             read_data="""
#     {
#             "user_stocks": ["AAPL"]
#     }
#     """
#         ),
#     )
#     def test_get_stock_prices(self, mock_request):
#         user_stocks = get_stock_prices("path/to/file.json")
#
#         self.assertEqual(user_stocks, {"stock": "AAPL", "price": 213.4})
#         # Настраиваем моки
#         mock_request_env.return_value = "test_api_key"
#         mock_response = mock.Mock()
#         mock_response.status_code = 200
#         mock_response.json.return_value = {"stock": "AAPL", "price": 213.4}
#         mock_request.return_value = mock_response
#
#         # Тестируем функцию
#         currencies_stocks_list = {
#             'user_currencies': ['USD', 'EUR', 'AED', 'CNY', 'GBP', 'CHF', 'KZT', 'BYN'],
#             'user_stocks': ['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'TSLA']
#                                   }
#         mock_response = get_stock_prices(currencies_stocks_list)
#
#         # Проверяем результат
#         expected_result = [
#             {"stock": "AAPL", "price": 213.4}
#         ]
#
#         self.assertEqual(mock_response, expected_result)
#         mock_request.assert_called_once_with("https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=test_api_key")
#
# class TestReadFile(unittest.TestCase):
#     @patch('builtins.open', new_callable=mock_open, read_data='file content')
#     def test_read_file(self, mock_file):
#         content = read_file('testfile.txt')
#         mock_file.assert_called_once_with('testfile.txt', 'r')
#         self.assertEqual(content, 'file content')
#
#
# def test_patch(mock_file):
#     assert open("path/to/open").read() == "data"
#     mock_file.assert_called_with("path/to/open")


class TestGetUserSetting(unittest.TestCase):
    @patch(
        "builtins.open",
        mock_open(
            read_data="""
    {
        "user_currencies": ["USD", "EUR", "AED", "CNY", "GBP", "CHF", "KZT", "BYN"],
        "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    }
    """
        ),
    )
    def test_get_user_setting(self):
        user_setting = get_user_setting("path/to/file.json")
        self.assertEqual(
            user_setting,
            {
                "user_currencies": ["USD", "EUR", "AED", "CNY", "GBP", "CHF", "KZT", "BYN"],
                "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"],
            },
        )
        # self.assertEqual(user_stocks, ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"])

    @patch(
        "builtins.open",
        mock_open(
            read_data="""
    {
        "user_currencies": [],
        "user_stocks": []
    }
    """
        ),
    )
    def test_get_user_setting_empty(self):
        user_setting = get_user_setting("path/to/file.json")
        self.assertEqual(user_setting, {"user_currencies": [], "user_stocks": []})
        # self.assertEqual(user_stocks, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_user_setting_file_not_found(self, mock_open):
        with self.assertRaises(FileNotFoundError):
            get_user_setting("path/to/file.json")


@patch("requests.get")
def test_get_currency_exchange_rates(mock_get, currencies_stocks_list):
    """Тестирование функции вывода курса валют"""
    mock_get.return_value.json.return_value = [
        {"currency": "USD", "rate": 110.85},
        {"currency": "EUR", "rate": 114.16},
        {"currency": "AED", "rate": 30.18},
        {"currency": "CNY", "rate": 15.12},
        {"currency": "GBP", "rate": 137.64},
        {"currency": "CHF", "rate": 121.92},
        {"currency": "KZT", "rate": 0.21},
        {"currency": "BYN", "rate": 33.23},
    ]
    assert get_currency_exchange_rates(currencies_stocks_list) == [
        {"currency": "USD", "rate": 110.85},
        {"currency": "EUR", "rate": 114.16},
        {"currency": "AED", "rate": 30.18},
        {"currency": "CNY", "rate": 15.12},
        {"currency": "GBP", "rate": 137.64},
        {"currency": "CHF", "rate": 121.92},
        {"currency": "KZT", "rate": 0.21},
        {"currency": "BYN", "rate": 33.23},
    ]


# def test_get_currency_exchange_rates_empty():
#     """Тестирование, если передан пустой список"""
#     result = get_currency_exchange_rates([])
#     assert result == []


@patch("requests.get")
def test_get_stock_prices(mock_get):
    """Тестирование функции получения данных об акциях"""
    mock_response = Mock()

    mock_response.json.return_value = [
        {"stock": "AAPL", "price": 213.8},
        {"stock": "AMZN", "price": 190.0},
        {"stock": "GOOGL", "price": 169.7},
        {"stock": "MSFT", "price": 425.2},
        {"stock": "TSLA", "price": 239.9},
    ]
    mock_get.return_value = mock_response
    stocks = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    expected_result = [
        {"stock": "AAPL", "price": 213.8},
        {"stock": "AMZN", "price": 190.0},
        {"stock": "GOOGL", "price": 169.7},
        {"stock": "MSFT", "price": 425.2},
        {"stock": "TSLA", "price": 239.9},
    ]

    result = get_stock_prices(stocks)
    assert result == expected_result


# def test_get_stock_prices_empty_list():
#     """Тестирование, если передан пустой словарь"""
#     result = get_stock_prices([])
#     expected = []
#     assert result == expected


# @patch('requests.get')
# def test_get_stock_prices_invalid_response(mock_get):
#     mock_response = Mock()
#     mock_response.json.return_value = [{"stock": "GOOGL", "price": "invalid_price"}]
#     mock_get.return_value = mock_response
#     stock = ["GOOGL"]
#     with pytest.raises(ValueError):
#         get_stock_prices(stock)
