from src.vacancy import Vacancy


def test_vacancy_init():
    """Тестируем инициализацию класса Vacancy"""
    vacancy_name = "Python Developer"
    area = "Москва"
    salary_from = 100000
    employer = "Компания A"
    url = "http://example.com"

    vacancy = Vacancy(vacancy_name, area, salary_from, employer, url)

    assert vacancy.vacancy_name == vacancy_name
    assert vacancy.area == area
    assert vacancy.salary_from == salary_from
    assert vacancy.employer == employer
    assert vacancy.url == url


def test_create_obj_list(vacancies_list_dict):
    """ """
    vacancies = Vacancy.create_obj_list(vacancies_list_dict)
    assert len(vacancies) == 2
    assert vacancies[0].vacancy_name == 'Аналитик-стажер (SQL)'


def test_validate_vacancy_name():
    """Тестируем метод валидации названия вакансии"""

    assert Vacancy._Vacancy__validate_vacancy_name("Python Developer") == "Python Developer"
    assert Vacancy._Vacancy__validate_vacancy_name("") == "Неизвестная вакансия"
    assert Vacancy._Vacancy__validate_vacancy_name(None) == "Неизвестная вакансия"
    assert Vacancy._Vacancy__validate_vacancy_name(123) == "Неизвестная вакансия"
    assert Vacancy._Vacancy__validate_vacancy_name([]) == "Неизвестная вакансия"
    assert Vacancy._Vacancy__validate_vacancy_name({}) == "Неизвестная вакансия"
