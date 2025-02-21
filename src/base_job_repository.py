from abc import ABC, abstractmethod


class BaseJobRepository(ABC):
    @abstractmethod
    def read_vacancies(self):
        pass

    @abstractmethod
    def add_vacancies(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        pass