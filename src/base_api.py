from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Базовый абстрактный класс для работы с API"""

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        """"""
        pass