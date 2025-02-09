from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Базовый абстрактный класс для работы с API"""

    @abstractmethod
    def send_request_by_base_url(self, *args, **kwargs):
        """Метод для отправки запроса на базовый URL и получения статус кода"""
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """"""
        pass