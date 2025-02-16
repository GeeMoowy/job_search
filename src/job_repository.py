from typing import List
from src.base_job_repository import BaseJobRepository
import json
from src.vacancy import Vacancy


class JobRepository(BaseJobRepository):
    """Класс для записи вакансий в JSON-файл"""

    def __init__(self, filename: str):
        self.filename = filename

    def add_vacancy(self, vacancies: List['Vacancy']):
        """Добавление списка вакансий в JSON-файл, избегая дубликатов"""
        # Преобразуем объекты Vacancy в словари
        vacancies_dicts = [self.vacancy_to_dict(vacancy) for vacancy in vacancies]
        existing_vacancies = self.get_vacancies()  # Получаем текущие вакансии

        # Создаем множество для хранения уникальных идентификаторов вакансий по URL
        id_by_url = {vacancy['url'] for vacancy in existing_vacancies}

        # Добавляем только уникальные вакансии
        for vacancy_dict in vacancies_dicts:
            if vacancy_dict['url'] not in id_by_url:  # Проверяем на дубликаты
                existing_vacancies.append(vacancy_dict)  # Добавляем новую вакансию

        with open(self.filename, 'w') as f:
            json.dump(existing_vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self, **criteria) -> List[dict]:
        """Получение вакансий по указанным критериям"""
        try:
            with open(self.filename, 'r') as f:
                vacancies = json.load(f)
                # Фильтрация по критериям (если указаны)
                if criteria:
                    return [vacancy for vacancy in vacancies if all(vacancy.get(k) == v for k, v in criteria.items())]
                return vacancies
        except FileNotFoundError:
            return []  # Если файл не найден, возвращаем пустой список

    def delete_vacancy(self, vacancy_name):
        """Удаление вакансии из JSON-файла"""
        vacancies = self.get_vacancies()
        vacancies = [vacancy for vacancy in vacancies if vacancy.get('name') != vacancy_name]  # Удаляем по id
        with open(self.filename, 'w') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    @staticmethod
    def vacancy_to_dict(vacancy: 'Vacancy') -> dict:
        """Преобразование объекта Vacancy в словарь"""
        return {
            'name': vacancy.vacancy_name,
            'area': vacancy.area,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'employer': vacancy.employer,
            'url': vacancy.url
        }

vacancy_file = JobRepository('data/my_vacancies.json')