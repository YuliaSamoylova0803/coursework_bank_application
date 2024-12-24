import pytest
from datetime import datetime


from src.views import get_greeting

test_date = [
    (datetime(2024, 12, 23, 7, 0), "Доброе утро"),
    (datetime(2024, 12, 23, 13, 0), "Добрый день"),
    (datetime(2024, 12, 23, 19, 0), "Добрый вечер"),
    (datetime(2024, 12, 23, 23, 30), "Доброй ночи"),
    (datetime(2024, 12, 23, 2, 0), "Доброй ночи")
]


@pytest.mark.parametrize("date_now, expected_greeting", test_date)
def test_get_greeting(date_now, expected_greeting):
    """Тестирование функции вывода приветствия в зависимости от времени суток"""
    assert get_greeting(date_now) == expected_greeting

