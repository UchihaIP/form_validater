import phonenumbers
from pydantic import  BaseModel, EmailStr
from pydantic.validators import strict_str_validator

from datetime import date


class PhoneNumber(str):
    """Валидация номера телефона, с использованием телефонных номеров Google"""

    @classmethod
    def __get_validators__(cls):
        yield strict_str_validator
        yield cls.validate

    @classmethod
    def validate(cls, v: str):
        # Remove spaces
        v = v.strip().replace(' ', '')

        try:
            pn = phonenumbers.parse(v)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError('invalid phone number format')

        return cls(phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164))


class Form(BaseModel):
    form_name: str | None
    email: EmailStr | None
    phone_number: PhoneNumber | None
    created_date: date | None
    text: str | None

    class Config:
        schema_extra = {
            "example": {
                "form_name": "MyForm",
                "email": "youemail@mail.ru",
                "phone_number": "+7 999 999 99 99",
                "created_date": "2022-01-06",
                "text": "some_text"
            }
        }

    @staticmethod
    def get_fields_type(fields: list) -> dict:
        """Выводит словарь 'поле - тип данных' для ложных query параметров."""
        types = {
            "form_name": str,
            "email": EmailStr,
            "phone_number": PhoneNumber,
            "created_date": date,
            "text": str
        }
        info_about_types = {item: str(types.get(item)) for item in fields
                            if item in types.keys()}
        if info_about_types:
            return info_about_types
        return {"info": "Таких полей не существует"}

