import random
import string

from asynctinydb import TinyDB, where
from pydantic import BaseSettings
from tinydb.table import Document

db = TinyDB("tiny_db.json")


class Database:
    def __init__(self, model):
        self.model = model

    async def find_form(self, fields, values) -> bool | Document:
        doc = await db.search((where(fields[0]) == values[0]) &
                              (where(fields[1]) == values[1]))
        if doc:
            return doc
        return False


class Settings(BaseSettings):
    async def initialize_database(self) -> None:
        """Если функция ниже не обнаружила БД в проекте,
        то инициализирует её и генерирует тестовые данные.
        """
        await db.insert_multiple(
            {"form_name": f"Form_template_number_{i}",
             "email": f"{self._generation_random_word(10)}@mail.ru",
             "phone_number": f"+7999{random.randint(int('1' * 7), int('9' * 7))}",
             "created_date": f"2022-{random.randint(1, 12)}-{random.randint(1, 31)}",
             "text": self._generation_random_word(10)}
            for i in range(31)
        )

    @staticmethod
    async def check_existence_of_data_in_database() -> bool:
        """Проверка, существует ли БД в данный момент."""
        check_data = await db.get(doc_id=1)
        if check_data:
            return True

    @staticmethod
    def _generation_random_word(length: int) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
