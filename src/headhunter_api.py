from typing import Any, Dict, List

import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """Класс подключается к API hh.ru и получает вакансии"""

    base_url: str
    headers: dict

    def __init__(self) -> None:
        """Конструктор метода для организации запроса на API hh.ru"""

        self.__base_url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}

    def __connect(self) -> requests.Response:
        """Метод для проверки подключения к API hh.ru"""

        response = requests.get(self.__base_url, headers=self.__headers)
        if response.status_code != 200:
            raise Exception(f"Ошибка подключения {response.status_code}")
        return response

    def get_vacancies(self, keyword: str) -> List[Dict[str, Any]]:
        """Метод получает вакансии сайта hh.ru по ключевому слову"""

        params = {'text': keyword, 'per_page': 20, 'area': 53}
        response = requests.get(self.__base_url, headers=self.__headers, params=params)  # Отправляем запрос на hh.ru

        if response.status_code != 200:
            raise Exception(f"Ошибка получения данных: {response.status_code}")

        vacancies = response.json().get('items', [])
        return vacancies
