from src.headhunter_api import HeadHunterAPI
from src.job_repository import JobRepository
from src.vacancy import Vacancy


api = HeadHunterAPI()
vacancy_data_list = api.get_vacancies('Python')

vacancy_instance = Vacancy('', '', 0, 0, '', '')
vacancies_objects = vacancy_instance.cast_to_object(vacancy_data_list)

for vacancy_res in vacancies_objects:
    print(vacancy_res.salary_from)

result = vacancy_instance.sort_by_salary(10)
for vacancy in result:
    print(vacancy.vacancy_name, vacancy.salary_from)

vac_file = JobRepository('data/my_vacancies.json')
res1 = vac_file.add_vacancy(result)
vac_by_criteria = vac_file.get_vacancies(salary_from=300000)
print(vac_by_criteria)
del_vac = vac_file.delete_vacancy("Data Science Engineer")
