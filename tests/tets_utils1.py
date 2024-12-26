import pytest

from src.utils import get_date


@pytest.mark.parametrize(
    "date, formatted_date",
    [
        ("16.02.2018", "2018-02-16"),
        ("01.01.2001", "2001-01-01"),
        ("1.02.2018", "2018-02-01"),
    ],
)
def test_get_date(date: str, formatted_date: str) -> str:
    """Функция тестирует вывод приветствия в зависимрсти от времени суток"""
    assert get_date(date) == formatted_date
