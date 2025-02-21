from unittest.mock import Mock

import pytest

from src.headhunter_api import HeadHunterAPI


@pytest.fixture
def api():
    return HeadHunterAPI()


def test_connect_success(api, mocker):
    """Тест успешного соединения с API"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': []}

    mocker.patch('requests.get', return_value=mock_response)

    response = api._HeadHunterAPI__connect()
    assert response == mock_response


def test_connect_failure(api, mocker):
    """Тест неудачного соединения с API"""
    mock_response = Mock()
    mock_response.status_code = 404

    mocker.patch('requests.get', return_value=mock_response)

    with pytest.raises(Exception) as excinfo:
        api._HeadHunterAPI__connect()
    assert "Ошибка подключения 404" in str(excinfo.value)


def test_get_vacancies_success(api, mocker):
    """Тест успешного получения вакансий"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'items': [{'name': 'Python Developer', 'url': 'http://example.com'}]}

    mocker.patch('requests.get', side_effect=[mock_response, mock_response])

    vacancies = api.get_vacancies("Python")
    assert len(vacancies) == 1
    assert vacancies[0]['name'] == 'Python Developer'


def test_get_vacancies_failure(api, mocker):
    """Тест неудачного получения вакансий"""
    mock_response = Mock()
    mock_response.status_code = 500

    mocker.patch('requests.get', side_effect=[mock_response, mock_response])

    with pytest.raises(Exception) as excinfo:
        api.get_vacancies("Python")
    assert "Ошибка получения данных: 500" in str(excinfo.value)
