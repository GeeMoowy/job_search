from abc import ABC, abstractmethod


class BaseJobRepository(ABC):
    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        pass