# Проект Form_validater
## Описание проекта 

Web-приложение для определения заполненных форм.

В базе данных ___tiny_db.json___ хранится список шаблонов форм.

Шаблон формы, это структура, которая задается уникальным набором полей, с указанием их типов.

Пример шаблона формы:
```
  {
    "name": "Form template name",
    "field_name_1": "email",
    "field_name_2": "phone"
  }
```

Всего должно поддерживаться четыре типа данных полей: 
email
телефон
дата
текст.

Все типы кроме текста должны поддерживать валидацию. Телефон передается в стандартном формате ___+7 xxx xxx xx xx___, дата передается в формате ___YYYY-MM-DD___.

На вход по урлу /get_form/ ___POST___ запросом передаются данные такого вида:
```
  f_name1=value1&f_name2=value2
```
В ответ возвращается имя шаблона формы, если она была найдена.
Чтобы нашелся подходящий шаблон нужно указать ___имя и тип___ значения вместо ___f_name и f_value___ соответственно. Совпадающими считаются поля, у которых совпали ___имя___ и ___тип___ значения.

Если подходящей формы не нашлось, возвращается ответ в следующем формате
```
  {
    f_name1: FIELD_TYPE,
    f_name2: FIELD_TYPE
  }
```
где ___FIELD_TYPE___ это ___тип___ поля, выбранный на основе правил валидации.


## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```bash
  git clone https://github.com/UchihaIP/form_validater.git
  cd form_validater
```

Cоздать и активировать виртуальное окружение:
```bash
  python3 -m venv env 
  source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```bash
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt
```

Запустить проект:
```bash
  python main.py
```

Запустить тесты (из тестов делаются запросы с тестовыми параметрами):
```bash
  python test.py
```

## API Reference

#### Получение информации о товаре

```http
  POST /get_item/?f_name1=value1&f_name2=value2
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `f_name1` | `str` | **Required** Поле шаблона формы|
| `value1` | `str` | **Required** Значения поля шаблона формы|
| `f_name2` | `str` | **Required** Поле шаблона формы|
| `value2` | `str` | **Required** Значения поля шаблона формы|


## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![TinyDB](https://img.shields.io/badge/TinyDB-22ADF6?style=for-the-badge&logo=TinyDB&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)


## Author

Рифат Хасанов
- [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/UchihaIP)
- [![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/lawlietLL)

