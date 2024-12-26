from src.reports import log, spending_by_category
from tests.conftest import df_transaction_1


def test_spending_by_category_with_date(data_for_tests):
    # Тестирование функции с указанной датой и категорией "Продукты"
    result = spending_by_category(data_for_tests, "Продукты", "30.12.2021 17:50:30")
    assert (
        len(result) == 1
    )  # Ожидается 1 строки, так как только две операции с категорией "Продукты" за последние три месяца от указанной даты


def test_spending_by_category_no_date(data_for_tests):
    result = spending_by_category(data_for_tests, "Продукты", "25.12.2021 18:45:00")
    assert len(result) == 1  # Ожидаем три строки, соответствующие категории "Продукты"


def test_spending_by_category_future_date(data_for_tests):
    # Тестирование функции с будущей датой
    result = spending_by_category(data_for_tests, "Супермаркеты", "01.02.2023 00:00:00")
    assert (
        len(result) == 0
    )  # Ожидается 0 строк, так как нет операций с категорией "Продукты" за последние три месяца от будущей даты


def test_spending_by_category_no_transactions(data_for_tests):
    # Тестирование функции с категорией, для которой нет транзакций
    result = spending_by_category(data_for_tests, "Фитнес", "30.12.2020 17:50:30")
    assert len(result) == 0  # Ожидается 0 строк, так как нет транзакций с категорией "Фитнес"


def test_spending_by_category_medicina(df_transaction_1):
    # Тестирование функции с категорией, для которой нет транзакций
    result = spending_by_category(df_transaction_1, "Медицина", "31.12.2021 17:50:30")
    assert len(result) == 2  # Ожидается 2 строк, так как транзакций с категорией "Медицина"


@log(filename="reports_file.txt")
def test_log_save_file():
    result = spending_by_category(df_transaction_1, "Медицина", "31.12.2021 17:50:30")
    assert len(result) == 2


def test_log_in_file() -> None:
    @log(filename="reports_file.txt")
    def my_function(x: int, y: int) -> int:
        """Функция суммирует два числа и возвращает результат"""
        return x + y

    my_function(2, 2)
    with open("reports_file.txt") as f:
        data = f.read().split("\n")[-2]
    assert data == "my_function ok"
