from pathlib import Path

from src.settings import BASE_DIR
from src.views import main

project_log = Path(BASE_DIR, "logs", "logs_file.txt")
stock_rates_path = Path(BASE_DIR, "src", "user_settings.json")


def test_main_ok():
    assert main() == ('{\n'
 '    "greeting": "Добрый вечер",\n'
 '    "cards": [\n'
 '        {\n'
 '            "last_digits": "*1112",\n'
 '            "total spent": 46207.08,\n'
 '            "cashback": 462.07\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*4556",\n'
 '            "total spent": 1780150.21,\n'
 '            "cashback": 17801.5\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*5091",\n'
 '            "total spent": 17367.5,\n'
 '            "cashback": 173.68\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*5441",\n'
 '            "total spent": 470854.8,\n'
 '            "cashback": 4708.55\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*5507",\n'
 '            "total spent": 84000.0,\n'
 '            "cashback": 840.0\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*6002",\n'
 '            "total spent": 69200.0,\n'
 '            "cashback": 692.0\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*7197",\n'
 '            "total spent": 2487419.56,\n'
 '            "cashback": 24874.2\n'
 '        }\n'
 '    ],\n'
 '    "top_transactions": [\n'
 '        {\n'
 '            "date": "21.03.2019",\n'
 '            "amount": -190044.51,\n'
 '            "category": "Переводы",\n'
 '            "description": "Перевод Кредитная карта. ТП 10.2 RUR"\n'
 '        },\n'
 '        {\n'
 '            "date": "27.07.2018",\n'
 '            "amount": -179571.56,\n'
 '            "category": NaN,\n'
 '            "description": "Перевод средств с брокерского счета"\n'
 '        },\n'
 '        {\n'
 '            "date": "28.07.2018",\n'
 '            "amount": -179571.56,\n'
 '            "category": NaN,\n'
 '            "description": "Перевод средств с брокерского счета"\n'
 '        },\n'
 '        {\n'
 '            "date": "27.07.2018",\n'
 '            "amount": -179571.56,\n'
 '            "category": NaN,\n'
 '            "description": "Перевод средств с брокерского счета"\n'
 '        },\n'
 '        {\n'
 '            "date": "23.10.2018",\n'
 '            "amount": -177506.03,\n'
 '            "category": "Переводы",\n'
 '            "description": "Перевод Кредитная карта. ТП 10.2 RUR"\n'
 '        }\n'
 '    ],\n'
 '    "currency_rates": [\n'
 '        {\n'
 '            "currency": "USD",\n'
 '            "rate": 103.32\n'
 '        },\n'
 '        {\n'
 '            "currency": "EUR",\n'
 '            "rate": 107.75\n'
 '        },\n'
 '        {\n'
 '            "currency": "AED",\n'
 '            "rate": 28.13\n'
 '        },\n'
 '        {\n'
 '            "currency": "CNY",\n'
 '            "rate": 14.16\n'
 '        },\n'
 '        {\n'
 '            "currency": "GBP",\n'
 '            "rate": 129.84\n'
 '        },\n'
 '        {\n'
 '            "currency": "CHF",\n'
 '            "rate": 114.66\n'
 '        },\n'
 '        {\n'
 '            "currency": "KZT",\n'
 '            "rate": 0.2\n'
 '        },\n'
 '        {\n'
 '            "currency": "BYN",\n'
 '            "rate": 31.65\n'
 '        }\n'
 '    ],\n'
 '    "stock_prices": []\n'
 '}') != ('{\n'
 '    "greeting": "Добрый вечер",\n'
 '    "cards": [\n'
 '        {\n'
 '            "last_digits": "*1112",\n'
 '            "total spent": 46207.08,\n'
 '            "cashback": 462.07\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*4556",\n'
 '            "total spent": 1780150.21,\n'
 '            "cashback": 17801.5\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*5091",\n'
 '            "total spent": 17367.5,\n'
 '            "cashback": 173.68\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*5441",\n'
 '            "total spent": 470854.8,\n'
 '            "cashback": 4708.55\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*5507",\n'
 '            "total spent": 84000.0,\n'
 '            "cashback": 840.0\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*6002",\n'
 '            "total spent": 69200.0,\n'
 '            "cashback": 692.0\n'
 '        },\n'
 '        {\n'
 '            "last_digits": "*7197",\n'
 '            "total spent": 2487419.56,\n'
 '            "cashback": 24874.2\n'
 '        }\n'
 '    ],\n'
 '    "top_transactions": [\n'
 '        {\n'
 '            "date": "21.03.2019",\n'
 '            "amount": -190044.51,\n'
 '            "category": "Переводы",\n'
 '            "description": "Перевод Кредитная карта. ТП 10.2 RUR"\n'
 '        },\n'
 '        {\n'
 '            "date": "27.07.2018",\n'
 '            "amount": -179571.56,\n'
 '            "category": NaN,\n'
 '            "description": "Перевод средств с брокерского счета"\n'
 '        },\n'
 '        {\n'
 '            "date": "28.07.2018",\n'
 '            "amount": -179571.56,\n'
 '            "category": NaN,\n'
 '            "description": "Перевод средств с брокерского счета"\n'
 '        },\n'
 '        {\n'
 '            "date": "27.07.2018",\n'
 '            "amount": -179571.56,\n'
 '            "category": NaN,\n'
 '            "description": "Перевод средств с брокерского счета"\n'
 '        },\n'
 '        {\n'
 '            "date": "23.10.2018",\n'
 '            "amount": -177506.03,\n'
 '            "category": "Переводы",\n'
 '            "description": "Перевод Кредитная карта. ТП 10.2 RUR"\n'
 '        }\n'
 '    ],\n'
 '    "currency_rates": [\n'
 '        {\n'
 '            "currency": "USD",\n'
 '            "rate": 103.32\n'
 '        },\n'
 '        {\n'
 '            "currency": "EUR",\n'
 '            "rate": 107.75\n'
 '        },\n'
 '        {\n'
 '            "currency": "AED",\n'
 '            "rate": 28.13\n'
 '        },\n'
 '        {\n'
 '            "currency": "CNY",\n'
 '            "rate": 14.16\n'
 '        },\n'
 '        {\n'
 '            "currency": "GBP",\n'
 '            "rate": 129.84\n'
 '        },\n'
 '        {\n'
 '            "currency": "CHF",\n'
 '            "rate": 114.66\n'
 '        },\n'
 '        {\n'
 '            "currency": "KZT",\n'
 '            "rate": 0.2\n'
 '        },\n'
 '        {\n'
 '            "currency": "BYN",\n'
 '            "rate": 31.65\n'
 '        }\n'
 '    ],\n'
 '    "stock_prices": [\n'
 '        {\n'
 '            "stock": "AAPL",\n'
 '            "price": 212.2\n'
 '        },\n'
 '        {\n'
 '            "stock": "AMZN",\n'
 '            "price": 189.1\n'
 '        },\n'
 '        {\n'
 '            "stock": "GOOGL",\n'
 '            "price": 168.7\n'
 '        },\n'
 '        {\n'
 '            "stock": "MSFT",\n'
 '            "price": 425.1\n'
 '        },\n'
 '        {\n'
 '            "stock": "TSLA",\n'
 '            "price": 235.1\n'
 '        }\n'
 '    ]\n'
 '}')


# def test_get_greeting_morning():
#     with pytest.raises(TypeError):
#         with patch("datetime.datetime.now") as mock_now:
#             mock_now.return_value = dt.datetime(2023, 4, 1, 8, 0, 0)
#             assert get_greeting() == "Доброе утро"
#
#
# def test_get_greeting_afternoon():
#     with pytest.raises(TypeError):
#         with patch("datetime.datetime.now") as mock_now:
#             mock_now.return_value = dt.datetime(2023, 4, 1, 14, 0, 0)
#             assert get_greeting() == "Добрый день"
#
#
# def test_get_greeting_evening():
#     with pytest.raises(TypeError):
#         with patch("datetime.datetime.now") as mock_now:
#             mock_now.return_value = dt.datetime(2023, 4, 1, 19, 0, 0)
#             assert get_greeting() == "Добрый вечер"
#
#
# def test_get_greeting_night():
#     with pytest.raises(TypeError):
#         with patch("datetime.datetime.now") as mock_now:
#             mock_now.return_value = dt.datetime(2023, 4, 1, 23, 0, 0)
#             assert get_greeting() == "Доброй ночи"


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
#         {'currency': 'USD', 'rate': 103.32},
#         {'currency': 'EUR', 'rate': 107.75},
#         {'currency': 'AED', 'rate': 28.13},
#         {'currency': 'CNY', 'rate': 14.16},
#         {'currency': 'GBP', 'rate': 129.84},
#         {'currency': 'CHF', 'rate': 114.66},
#         {'currency': 'KZT', 'rate': 0.2},
#         {'currency': 'BYN', 'rate': 31.65}
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
#         {'stock': 'AAPL', 'price': 212.2},
#         {'stock': 'AMZN', 'price': 189.1},
#         {'stock': 'GOOGL', 'price': 168.7},
#         {'stock': 'MSFT', 'price': 425.1},
#         {'stock': 'TSLA', 'price': 235.1}
#     ]
