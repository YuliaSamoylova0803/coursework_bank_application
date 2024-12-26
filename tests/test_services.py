import json

import pytest

from src.services import search_transactions_for_individuals


def test_search_transactions_for_individuals_success(sample_dict_transaction):
    pattern = r"Константин Л."
    result = search_transactions_for_individuals(sample_dict_transaction, pattern)
    expected = json.dumps(
        [
            {"Описание": "Константин Л."},
        ],
        ensure_ascii=False,
    )
    assert result == expected


def test_search_transactions_for_individuals_no_match(sample_dict_transaction):
    """Проверка если в списке нет данных соответствующих паттерну, выводим пустой список"""
    pattern = r"Аптеки"
    result = search_transactions_for_individuals(sample_dict_transaction, pattern)
    expected = []
    assert result == expected


def test_search_transactions_for_individuals_empty_input():
    """Проверка, паттерн корректный но нет данных"""
    pattern = r"Константин Л."
    expected_result = []

    result = search_transactions_for_individuals([], pattern)
    assert result == expected_result


@pytest.mark.parametrize(
    "dict_transaction, pattern, expected_output",
    [
        (
            [
                {"Описание": "Перевод физлицу"},
                {"Описание": "Оплата услуги"},
                {"Описание": "Перевод физлицу на сумму 1000"},
            ],
            r"Перевод физлицу",
            json.dumps(
                [
                    {"Описание": "Перевод физлицу"},
                    {"Описание": "Перевод физлицу на сумму 1000"},
                ],
                ensure_ascii=False,
            ),
        ),
        (
            [
                {"Описание": "Оплата кредита"},
                {"Описание": "Оплата услуги"},
            ],
            r"Перевод физлицу",
            [],
        ),
        (
            [
                {"Описание": "Перевод физлицу"},
                {"Описание": "Перевод физлицу"},
            ],
            r"Перевод физлицу",
            json.dumps(
                [
                    {"Описание": "Перевод физлицу"},
                    {"Описание": "Перевод физлицу"},
                ],
                ensure_ascii=False,
            ),
        ),
    ],
)
def test_search_transactions_for_individuals(dict_transaction, pattern, expected_output):

    result = search_transactions_for_individuals(dict_transaction, pattern)

    assert result == expected_output
