import pytest


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