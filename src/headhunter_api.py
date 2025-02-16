import requests

from src.base_api import BaseAPI


class HeadHunterAPI(BaseAPI):
    """Класс подключается к API hh.ru и получает вакансии"""

    def __init__(self):
        """Конструктор метода для организации запроса на API hh.ru"""
        self.__base_url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}

    def send_request_by_base_url(self):
        """Метод для проверки подключения к API hh.ru"""
        try:
            response = requests.get(self.__base_url, headers=self.__headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к {self.__base_url}: {e}")
            return None

    def get_vacancies(self, keyword: str):
        """"""
        params = {'text': keyword, 'per_page': 10, 'area': 53}
        try:
            response = requests.get(self.__base_url, headers=self.__headers, params=params)  #Отправляем запрос на hh.ru
            print(f'Статус кода: {response.status_code}')  #Проверяем и печатаем статус кода
            vacancies_data = response.json()  # Преобразуем ответ в формат json
            if "items" in vacancies_data:
                vacancies_list = [{"item": item} for item in vacancies_data["items"]]
                return vacancies_list
            else:
                return "Ключ 'items' отсутствует"
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к {self.__base_url}: {e}")
            return None

hh_api = HeadHunterAPI()
print(hh_api)
vacancies_hh = hh_api.get_vacancies('Python')
print(vacancies_hh)
