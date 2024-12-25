import pytest


@pytest.fixture
def exchange_rates():
    return [
        {'currency': 'USD', 'rate': 100.1743},
        {'currency': 'EUR', 'rate': 104.1774},
        {'currency': 'AED', 'rate': 27.2769},
        {'currency': 'CNY', 'rate': 13.728},
        {'currency': 'GBP', 'rate': 125.6788},
        {'currency': 'CHF', 'rate': 111.3147},
        {'currency': 'KZT', 'rate': 0.1938},
        {'currency': 'BYN', 'rate': 29.8479}
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