import json
import os
from typing import Any, Dict, List

from src.base_job_repository import BaseJobRepository
from src.vacancy import Vacancy


class JobRepository(BaseJobRepository):
    """Класс для записи вакансий в JSON-файл"""

    filename: str

    def __init__(self, filename: str = 'data/my_vacancies.json') -> None:
        """Конструктор класса JobRepository"""

        self.__filename: str = filename

    def read_vacancies(self) -> List[Dict[str, Any]]:
        """Получение вакансий из файла"""

        if not os.path.exists(self.__filename):
            return []
        with open(self.__filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def add_vacancies(self, vacancies: List[Vacancy]) -> None:
        """Добавление списка вакансий в JSON-файл, избегая дубликатов"""

        existing_data = self.read_vacancies()
        existing_url = {vacancy['url'] for vacancy in existing_data}

        new_vacancies = []
        for vacancy in vacancies:
            vacancy_dict = self.vacancy_to_dict(vacancy)
            if vacancy_dict['url'] not in existing_url:  # Проверяем на дубликаты
                new_vacancies.append(vacancy_dict)

        if new_vacancies:  # Если есть новые вакансии, добавляем их в файл
            existing_data.extend(new_vacancies)
            with open(self.__filename, 'w', encoding='utf-8') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
            print(f"Добавлено {len(new_vacancies)} новых вакансий.")
        else:
            print("Нет новых вакансий для добавления.")

    def delete_vacancy(self) -> None:
        """Удаление всех вакансий из JSON-файла"""
        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)  # Записываем пустой список
        print("Все вакансии были удалены.")

    @staticmethod
    def vacancy_to_dict(vacancy: 'Vacancy') -> Dict[str, Any]:
        """Преобразование объекта Vacancy в словарь"""
        return {
            'name': vacancy.vacancy_name,
            'area': vacancy.area,
            'salary_from': vacancy.salary_from,
            'employer': vacancy.employer,
            'url': vacancy.url
        }
