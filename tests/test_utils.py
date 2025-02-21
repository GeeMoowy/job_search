import pytest
from src.utils import filter_by_words, top_vacancies, filter_by_salary
from src.vacancy import Vacancy


def test_filter_by_words(vacancy_list):
    """Тестирование функции фильтрации по ключевым словам."""
    filtered = filter_by_words(vacancy_list, ["Python"])
    assert len(filtered) == 1
    assert filtered[0].vacancy_name == "Python Developer"

    # Тест на отсутствие совпадений
    with pytest.raises(ValueError, match='Совпадения по ключевым слова не найдены'):
        filter_by_words(vacancy_list, ["C++"])

def test_top_vacancies(vacancy_list):
    """Тестирование функции получения топ N вакансий по зарплате."""
    top = top_vacancies(vacancy_list, 2)
    assert len(top) == 2
    assert top[0].vacancy_name == "Java Developer"  # Должен быть с самой высокой зарплатой
    assert top[1].vacancy_name == "Data Scientist"

def test_filter_by_salary(vacancy_list):
    """Тестирование функции фильтрации по диапазону зарплат."""
    filtered = filter_by_salary(vacancy_list, "100000 - 120000")
    assert len(filtered) == 3  # Должны остаться Python и Data Scientist

    filtered = filter_by_salary(vacancy_list, "110000 - 130000")
    assert len(filtered) == 2  # Должны остаться Java и Data Scientist

    filtered = filter_by_salary(vacancy_list, "150000 - 200000")
    assert len(filtered) == 0  # Не должно быть вакансий

    # Тест на неверный формат
    result = filter_by_salary(vacancy_list, "неверный формат")
    assert result == []  # Должно вернуть пустой список