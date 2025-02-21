

class Vacancy:
    """Класс для работы с вакансиями"""
    vacancy_name: str
    area: str
    salary_from: float
    employer: str
    url: str
    vacancies_list: list

    __slots__ = ("__vacancy_name", "__area", "__salary_from", "__employer", "__url", "__vacancies_list")

    def __init__(self, vacancy_name, area, salary_from, employer, url):
        """Конструктор вакансий"""
        self.__vacancy_name = self.__validate_vacancy_name(vacancy_name)
        self.__area = self.__validate_area(area)
        self.__salary_from = self.__validate_salary_from(salary_from)
        self.__employer = self.__validate_employer(employer)
        self.__url = self.__validate_url(url)
        self.__vacancies_list = []


    @staticmethod
    def __validate_vacancy_name(vacancy_name):
        """Валидация названия вакансии"""
        if not vacancy_name or not isinstance(vacancy_name, str):
            return 'Неизвестная вакансия'
        return vacancy_name

    @staticmethod
    def __validate_area(area):
        """Валидация области вакансии"""
        if not area or not isinstance(area, str):
            return 'Неизвестная область'
        return area

    @staticmethod
    def __validate_salary_from(salary_from):
        """Валидация области вакансии"""
        if not salary_from or salary_from < 0:
            return 0
        return salary_from

    @staticmethod
    def __validate_employer(employer):
        """Валидация области вакансии"""
        if not employer or not isinstance(employer, str):
            return 'Неизвестный работодатель'
        return employer

    @staticmethod
    def __validate_url(url):
        """Валидация области вакансии"""
        if not url or not isinstance(url, str):
            return 'Неизвестная ссылка'
        return url

    @classmethod
    def create_obj_list(cls, vacancies_list):
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

    def add_vacancy(self, vacancy):
        """Метод для добавления объекта вакансии в список"""
        if isinstance(vacancy, Vacancy):
            self.__vacancies_list.append(vacancy)
        else:
            raise ValueError("Добавляемый объект должен быть экземпляром класса Vacancy")

    def get_vacancies(self):
        """Метод для получения списка вакансий"""
        return self.__vacancies_list

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (меньше)"""
        return self.__salary_from < other.__salary_from

    def __le__(self, other):
        """Сравнение вакансий по зарплате (меньше или равно)"""
        return self.__salary_from <= other.__salary_from

    def __gt__(self, other):
        """Сравнение вакансий по зарплате (больше)"""
        return self.__salary_from > other.__salary_from

    def __ge__(self, other):
        """Сравнение вакансий по зарплате (больше или равно)"""
        return self.__salary_from >= other.__salary_from

    def __eq__(self, other):
        """Сравнение вакансий по зарплате (равно)"""
        return self.__salary_from == other.__salary_from

    @property
    def vacancy_name(self):
        return self.__vacancy_name

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def employer(self):
        return self.__employer

    @property
    def url(self):
        return self.__url

    @property
    def area(self):
        return self.__area


    # def __repr__(self):
    #     """Строковое представление вакансии"""
    #     return (f"Vacancy(title={self.__vacancy_name}, salary={self.__salary_from}, company={self.__employer}, "
    #             f"location={self.__area}, url={self.__url})")
