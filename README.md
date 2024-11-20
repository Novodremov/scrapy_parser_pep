# Асинхронный парсер PEP

## Описание
Парсер асинхронно собирает информацию о статусах существующих PEP.

### Функции парсера:

* Сбор статусов существующих PEP, подсчёт количества PEP с каждым из статусов;
* Вывод результатов работы в csv-файлы.


## Применяемые технологии

```
python 3.9
scrapy
```

### Порядок действия для запуска парсера

Клонировать репозиторий:

```bash
git clone git@github.com:Novodremov/scrapy_parser_pep.git
```

Перейти в папку с проектом:


```bash
cd scrapy_parser_pep
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

* Для Linux/MacOS

    ```bash
    source venv/bin/activate
    ```

* Для Windows

    ```bash
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

## Работа с парсером

Сбор статусов существующих PEP, подсчёт количества PEP с каждым из статусов:
```bash
scrapy crawl pep
```

## Создаваемые в процессе работы парсера директории:
* _results_ - выгрузка csv-файлов.

## Автор
Лысов Алексей