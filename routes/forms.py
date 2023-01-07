import logging
from typing import Literal
import sys

from fastapi import APIRouter, Request

from database.connection import Database
from models.forms import Form

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

form_router = APIRouter(
    tags=["form"]
)

form_database = Database(Form)


@form_router.post("/get_form/", response_model_include={"form_name"})
async def get_form(request: Request) -> dict[Literal["form_name"], str] | dict:
    """Получение имени формы по входным query параметрам (поле - значение).
    Если совпадения 'поле - значение' с формой отсутствуют,
    то выводит словарь: 'поле - тип данных'
    """
    logging.info("Сделан запрос по /get_form/")
    params = request.query_params
    fields, values = list(params.keys()), list(params.values())
    logging.info(f"Параметры запроса /get_form/ {fields=}, {values=}")
    form = await form_database.find_form(fields, values)
    if form:
        logging.info("Соответствие полей с шаблоном найдены успешно!")
        return {
            "form_name": form[0]["form_name"]
        }
    logging.info("Имя шаблона не найдено")
    return Form.get_fields_type(fields)
