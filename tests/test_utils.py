import pytest
import datetime
import datetime as dt
from pathlib import Path
from src.settings import BASE_DIR
from src.utils import get_date, get_excel_dataframe, get_dict_transaction, get_expenses_cards, top_transactions
import unittest
import pandas as pd
import json
from unittest.mock import Mock, patch


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
        {'amount': -20000.0, 'category': 'Переводы', 'date': '30.12.2021', 'description': 'Константин Л.'},
        {'amount': -800.0, 'category': 'Переводы', 'date': '31.12.2021', 'description': 'Константин Л.'},
        {'amount': -564.0, 'category': 'Различные товары', 'date': '31.12.2021', 'description': 'Ozon.ru'},
        {'amount': -160.89, 'category': 'Супермаркеты', 'date': '31.12.2021', 'description': 'Колхоз'},
        {'amount': -118.12, 'category': 'Супермаркеты', 'date': '31.12.2021', 'description': 'Магнит'}]


def test_top_transactions(top_trans_data):
    assert len(top_transactions(top_trans_data)) == 5


def test_top_transaction_empty_list():
    """Тест на случай, если передан пустой список транзакций."""
    with pytest.raises(TypeError):
        top_transactions()


