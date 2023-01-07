import requests

import unittest


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        cls.url = "http://127.0.0.1:8080/get_form/"

    def test_response_with_right_params(self):
        """Тестирование с правильными параметрами в запросе"""
        response = requests.post(url=self.url, headers=self.headers,
                                 params={
                                     "phone_number": "+79998210634",
                                     "email": "tzeeghzdwf@mail.ru"
                                 })

        self.assertEqual({'form_name': 'Form_template_number_3'}, response.json())
        print(f"Запрос по адресу: {response.url} \n"
              f"Вернул ответ {response.json()}\n"
              f"------------------------------")

        response = requests.post(url=self.url, headers=self.headers,
                                 params={
                                     "email": "jtqtueiaog@mail.ru",
                                     "created_date": "2022-2-25"
                                 })
        self.assertEqual({"form_name": "Form_template_number_2"}, response.json())
        print(f"Запрос по адресу: {response.url} \n"
              f"Вернул ответ {response.json()}\n"
              f"------------------------------")

        response = requests.post(url=self.url, headers=self.headers,
                                 params={
                                     "created_date": "2022-2-11",
                                     "text": "lyeqsttpje"
                                 })
        self.assertEqual({'form_name': 'Form_template_number_3'}, response.json())
        print(f"Запрос по адресу: {response.url} \n"
              f"Вернул ответ {response.json()}\n"
              f"------------------------------")

    def test_response_with_wrong_parameter(self):
        """Тестирование с неверными параметрами в запросе"""
        response = requests.post(url=self.url, headers=self.headers,
                                 params={
                                     "email": "jteiaog@mail.ru",
                                     "created_date": "2022-2-5"
                                 })

        self.assertEqual({'created_date': "<class 'datetime.date'>",
                          'email': "<class 'pydantic.networks.EmailStr'>"}, response.json())
        print(f"Запрос по адресу: {response.url} \n"
              f"Вернул ответ {response.json()}\n"
              f"------------------------------")

        response = requests.post(url=self.url, headers=self.headers,
                                 params={
                                     "created_date": "2011-2-11",
                                     "text": "lyeqhjssfstpje"
                                 })
        self.assertEqual({'created_date': "<class 'datetime.date'>",
                          'text': "<class 'str'>"}, response.json())
        print(f"Запрос по адресу: {response.url} \n"
              f"Вернул ответ {response.json()}\n"
              f"------------------------------")

        response = requests.post(url=self.url, headers=self.headers,
                                 params={
                                     "phone_number": "+79998232634",
                                     "email": "tzerehzdwf@mail.ru"
                                 })
        self.assertEqual({'email': "<class 'pydantic.networks.EmailStr'>",
                          'phone_number': "<class 'models.forms.PhoneNumber'>"}, response.json())
        print(f"Запрос по адресу: {response.url} \n"
              f"Вернул ответ {response.json()}\n"
              f"------------------------------")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Well done! Tests accepted!")
