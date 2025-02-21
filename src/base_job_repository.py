from abc import ABC, abstractmethod
from typing import List, Dict, Any

from src.vacancy import Vacancy


class BaseJobRepository(ABC):
    """Абстрактный класс для работы с хранилищем вакансий"""

    @abstractmethod
    def read_vacancies(self) -> List[Dict[str, Any]]:
        """Абстрактный метод чтения из файла для реализации в дочернем классе"""
        pass

    @abstractmethod
    def add_vacancies(self, vacancies: List[Vacancy]) -> None:
        """Абстрактный метод добавления вакансий в файл для реализации в дочернем классе"""
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs) -> None:
        """Абстрактный метод удаления вакансий из файла для реализации в дочернем классе"""
        pass
