from src.headhunter_api import HeadHunterAPI


class Vacancy:
    """Класс для работы с вакансиями"""
    vacancies_count = 0
    __slots__ = ("vacancy_name", "area", "salary_from", "salary_to", "employer", "url", "vacancies_obj")

    def __init__(self, vacancy_name, area, salary_from, salary_to, employer, url):
        """Конструктор вакансий"""
        self.vacancy_name = vacancy_name
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.url = url
        self.vacancies_obj = []
        Vacancy.vacancies_count += 1

    def cast_to_object(self, vacancy_list):
        for vacancy in vacancy_list:
            item = vacancy.get('item')
            if item:  # Проверяем, что item не None
                salary = item.get('salary')  # Получаем объект salary
                vacancy_add = Vacancy(
                    vacancy_name=item.get('name'),
                    area=item.get('area', {}).get('name'),
                    salary_from=salary.get('from') if salary else 0,
                    salary_to=salary.get('to') if salary else 0,
                    employer=item.get('employer', {}).get('name'),
                    url=item.get('url')
                )
                self.vacancies_obj.append(vacancy_add)
        return self.vacancies_obj

    def sort_by_salary(self, top_by_salary: int):
        self.vacancies_obj = sorted(self.vacancies_obj, key=lambda v: v.salary_from, reverse=True)
        res = self.vacancies_obj[0:top_by_salary]
        return res
#
#
# api = HeadHunterAPI()
# vacancy_data_list = api.get_vacancies('Python')
#
# vacancy_instance = Vacancy('', '', 0, 0, '', '')
# vacancies_objects = vacancy_instance.cast_to_object(vacancy_data_list)
#
# for vacancy_res in vacancies_objects:
#     print(vacancy_res.salary_from)
#
# result = vacancy_instance.sort_by_salary(3)
# for vacancy in result:
#     print(vacancy.vacancy_name, vacancy.salary_from)
