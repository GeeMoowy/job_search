from src.headhunter_api import HeadHunterAPI
from src.vacancy import Vacancy
import pandas as pd

hh_api = HeadHunterAPI()
print(hh_api)
python_vac = hh_api.get_vacancies('Python')
print(python_vac)
res = python_vac.create_vacancies
print(res)
