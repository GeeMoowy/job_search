from typing import List


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("__vacancy_name", "__area", "__salary_from", "__employer", "__url", "__vacancies_list")

    def __init__(self, vacancy_name: str, area: str, salary_from: float, employer: str, url: str):
        """Конструктор вакансий"""

        self.__vacancy_name = self.__validate_vacancy_name(vacancy_name)
        self.__area = self.__validate_area(area)
        self.__salary_from = self.__validate_salary_from(salary_from)
        self.__employer = self.__validate_employer(employer)
        self.__url = self.__validate_url(url)
        self.__vacancies_list: List['Vacancy'] = []

    @staticmethod
    def __validate_vacancy_name(vacancy_name: str) -> str:
        """Валидация названия вакансии"""
        if not vacancy_name or not isinstance(vacancy_name, str):
            return 'Неизвестная вакансия'
        return vacancy_name

    @staticmethod
    def __validate_area(area: str) -> str:
        """Валидация области вакансии"""
        if not area or not isinstance(area, str):
            return 'Неизвестная область'
        return area

    @staticmethod
    def __validate_salary_from(salary_from: float) -> float:
        """Валидация области вакансии"""
        if not salary_from or salary_from < 0:
            return 0
        return salary_from

    @staticmethod
    def __validate_employer(employer: str) -> str:
        """Валидация области вакансии"""
        if not employer or not isinstance(employer, str):
            return 'Неизвестный работодатель'
        return employer

    @staticmethod
    def __validate_url(url: str) -> str:
        """Валидация области вакансии"""
        if not url or not isinstance(url, str):
            return 'Неизвестная ссылка'
        return url

    @classmethod
    def create_obj_list(cls, vacancies_list: List[dict]) -> List['Vacancy']:
        """Создание списка объектов Vacancy из списка словарей"""

        object_list = []
        for item in vacancies_list:
            vacancy_name = item['name']
            area = item.get('area', {}).get('name', 'Неизвестная область')
            # Проверяем наличие 'salary' и его значение
            salary_from = item.get('salary', {})
            salary_from = salary_from.get('from', 0) if salary_from else 0  # Установим 0, если зарплата не указана
            employer = item.get('employer', {}).get('name', 'Неизвестный работодатель')
            url = item.get('alternate_url', 'Нет URL')  # Установим значение по умолчанию
            vacancy = cls(vacancy_name, area, salary_from, employer, url)
            object_list.append(vacancy)

        return object_list

    def add_vacancy(self, vacancy: 'Vacancy') -> None:
        """Метод для добавления объекта вакансии в список"""

        if isinstance(vacancy, Vacancy):
            self.__vacancies_list.append(vacancy)
        else:
            raise ValueError("Добавляемый объект должен быть экземпляром класса Vacancy")

    def get_vacancies(self) -> List['Vacancy']:
        """Метод для получения списка вакансий"""
        return self.__vacancies_list

    def __lt__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (меньше)"""
        return self.__salary_from < other.__salary_from

    def __le__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (меньше или равно)"""
        return self.__salary_from <= other.__salary_from

    def __gt__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (больше)"""
        return self.__salary_from > other.__salary_from

    def __ge__(self, other: 'Vacancy') -> bool:
        """Сравнение вакансий по зарплате (больше или равно)"""
        return self.__salary_from >= other.__salary_from

    def __eq__(self, other: object) -> bool:
        """Сравнение вакансий по зарплате (равно)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.__salary_from == other.__salary_from

    @property
    def vacancy_name(self) -> str:
        """Геттер для получения названия вакансии"""
        return self.__vacancy_name

    @property
    def salary_from(self) -> float:
        """Геттер для получения суммы зарплаты"""
        return self.__salary_from

    @property
    def employer(self) -> str:
        """Геттер для получения названия компании"""
        return self.__employer

    @property
    def url(self) -> str:
        """Геттер для получения ссылки на вакансию"""
        return self.__url

    @property
    def area(self) -> str:
        """Геттер для получения области вакансии"""
        return self.__area
