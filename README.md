## Курсовая работа "Личный кабинет клиента банка"

+ Приложение для анализа транзакций, которые находятся в Excel-файле.
+ Приложение генерирует JSON-данные для веб-страниц. 
+ Формирует Excel-отчеты, курсы валют, цены на акции, на Python. 

## Используются следующие зависимости:
poetry init

poetry add --group lint flake8 black mypy isort 
- requests
- pandas
- os
- json
- openpyxl
- pytest
- logging
- pathlib
- datetime
- unittest
- re


## Использование:
+ Приложение работает с данными из Excel-файле, при желании можно загрузить и свои данные
+ Страница «Главная», «Сервисы» - Поиск переводов физическим лицам, «Отчеты» - Траты по категории
+ Функции для главной страницы расположены в модуле views.py, часть вспомогательных в модуле utils, 
+ Сервис и Отчет реализованы в модулях services.py и reports.py соответственно.
+ Функции написаны исходя из моих возможностей (совсем ни понимаю сортировку), знаний, времени и сил на момент написания (26.12.2024) просто каша в голове и накопленная усталость
+ Тесты запускала в терминале через pytest, все проходили. Попыталась использовать mock b patch, параметризацию и фикстуры
+ Для путей добавлен отдельно файл settings.py
+ Добавлены логгеры, запись и в файл и в консоль, и settings к ним, поработала с basicConfig.
+ В модуле views находятся функция приветствия get_greeting, получения курса валют и цен на акции соответственно get_currency_exchange_rates и get_stock_prices. Используются библиотеки requests, datetime
+ Модуль utils вспомогательный: функция преобразования даты, чтения excel файла, преобразования в словарь и подсчет затрат и топ 5 транзакций.
+ Модуль services представлен функцией Поиск переводов физическим лицам, используется библиотека re и json
+ Reports модуль для отчета: прописана функция поиска по категориям.
+ Добавлена основная логика в функции main, которая представлена в модуле views
+ Программа запускается через if __name__ == "__main__":
    print(main()) и выдает json-ответ

## Проверка группой линтеров:
* При запуске линтера Flake8 обнаружено 2 ошибки про длинные строчки.
* При проверке линтером mypy выводится много ошибок.
* Isort поправил в коде импорты.

## Тестирование
Тестами покрыто 90 % кода. Все тесты завершаются ожидаемым образом

## Документация:
Дополнительную информацию о структуре проекта и API можно найти в документации.

## Команда проекта:
+ **Юлия Самойлова** - Python-разработчик 
+ **Команда SkyPro**