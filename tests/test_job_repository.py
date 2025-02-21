import os
import json
import pytest
from src.job_repository import JobRepository
from src.vacancy import Vacancy

@pytest.fixture
def job_repository(tmp_path):
    """Фикстура для создания временного репозитория вакансий."""
    return JobRepository(filename=str(tmp_path / "test_vacancies.json"))

def test_read_vacancies_empty(job_repository):
    """Тест на чтение вакансий из пустого файла."""
    vacancies = job_repository.read_vacancies()
    assert vacancies == []

def test_read_vacancies_with_data(job_repository):
    """Тест на чтение вакансий из файла с данными."""
    test_data = [
        {'name': 'Python Developer', 'area': 'Remote', 'salary_from': 100000, 'employer': 'Company A', 'url': 'http://example.com/1'},
        {'name': 'Java Developer', 'area': 'Remote', 'salary_from': 120000, 'employer': 'Company B', 'url': 'http://example.com/2'},
    ]
    with open(job_repository._JobRepository__filename, 'w', encoding='utf-8') as f:
        json.dump(test_data, f, ensure_ascii=False, indent=4)

    vacancies = job_repository.read_vacancies()
    assert vacancies == test_data

def test_add_vacancies(job_repository):
    """Тест на добавление вакансий в файл."""
    vacancy1 = Vacancy("Python Developer", "Remote", 100000, "Company A", "http://example.com/1")
    vacancy2 = Vacancy("Java Developer", "Remote", 120000, "Company B", "http://example.com/2")
    job_repository.add_vacancies([vacancy1, vacancy2])

    vacancies = job_repository.read_vacancies()
    assert len(vacancies) == 2

def test_delete_vacancy(job_repository):
    """Тест на удаление всех вакансий из файла."""
    vacancy1 = Vacancy("Python Developer", "Remote", 100000, "Company A", "http://example.com/1")
    job_repository.add_vacancies([vacancy1])
    job_repository.delete_vacancy()

    vacancies = job_repository.read_vacancies()
    assert vacancies == []  # Файл должен быть пустым