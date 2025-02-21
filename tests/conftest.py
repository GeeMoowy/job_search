import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancies_list_dict():
    return [{'id': '117543238', 'premium': False, 'name': 'Аналитик-стажер (SQL)', 'department': None,
             'has_test': False, 'response_letter_required': False, 'area': {'id': '53', 'name': 'Краснодар',
                                                                            'url': 'https://api.hh.ru/areas/53'},
             'salary': {'from': 60000, 'to': None, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2025-02-21T07:32:19+0300',
             'created_at': '2025-02-21T07:32:19+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=117543238',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/117543238?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/117543238', 'relations': [],
             'employer': {'id': '1245158', 'name': 'МФК Саммит', 'url': 'https://api.hh.ru/employers/1245158',
                          'alternate_url': 'https://hh.ru/employer/1245158',
                          'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/3244532.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/3244533.png',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/700854.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1245158',
                          'accredited_it_employer': True, 'trusted': True},
             'snippet': {'requirement': 'Высшее образование, либо последний курс университета по техническим '
                                        'специальностям "математика", "физика", "информатика" обязательно. - '
                                        'Базовые знания SQL. - R / <highlighttext>Python</highlighttext>, '
                                        'как преимущество. - ', 'responsibility': '...и анализ качества кредитного '
                                                                                  'портфеля и эффективности действующих'
                                                                                  ' кредитных политик. - Анализ рынка '
                                                                                  'и конкурентной среды. - Построение '
                                                                                  'скоринговых моделей '
                                                                                  '(R/<highlighttext>Python</highlighttext>).'},
             'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'fly_in_fly_out_duration': [], 'work_format': [{'id': 'REMOTE', 'name': 'Удалённо'}],
             'working_hours': [{'id': 'HOURS_8', 'name': '8\xa0часов'}],
             'work_schedule_by_days': [{'id': 'FIVE_ON_TWO_OFF', 'name': '5/2'}], 'night_shifts': False,
             'professional_roles': [{'id': '10', 'name': 'Аналитик'}], 'accept_incomplete_resumes': True,
             'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
             'employment': {'id': 'full', 'name': 'Полная занятость'},
             'employment_form': {'id': 'FULL', 'name': 'Полная'}, 'internship': True, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '117494908', 'premium': False, 'name': 'Python-разработчик (FastApi)', 'department': None,
             'has_test': True, 'response_letter_required': False, 'area': {'id': '53', 'name': 'Краснодар',
                                                                           'url': 'https://api.hh.ru/areas/53'},
             'salary': None, 'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Краснодар', 'street': 'Северная улица', 'building': '405', 'lat': 45.037451,
                         'lng': 38.995678, 'description': None, 'raw': 'Краснодар, Северная улица, 405', 'metro': None,
                         'metro_stations': [], 'id': '652260'}, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2025-02-19T19:48:09+0300', 'created_at': '2025-02-19T19:48:09+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=117494908',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/117494908?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/117494908', 'relations': [],
             'employer': {'id': '596426', 'name': 'Russian Robotics', 'url': 'https://api.hh.ru/employers/596426',
                          'alternate_url': 'https://hh.ru/employer/596426',
                          'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/6349574.png',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/1182287.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/6349575.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=596426',
                          'accredited_it_employer': True, 'trusted': True},
             'snippet': {'requirement': 'Высшее образование (профильное или физико-математическое). Опыт работы c '
                                        'асинхронным FastApi от года. Знание библиотек SQLAlchemy и Pydantic. ',
                         'responsibility': 'Разработка модулей, компонентов, скриптов и API на '
                                           '<highlighttext>Python</highlighttext>.'},
             'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'fly_in_fly_out_duration': [], 'work_format': [{'id': 'REMOTE', 'name': 'Удалённо'}],
             'working_hours': [{'id': 'HOURS_8', 'name': '8\xa0часов'}],
             'work_schedule_by_days': [{'id': 'FIVE_ON_TWO_OFF', 'name': '5/2'}], 'night_shifts': False,
             'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'},
             'employment_form': {'id': 'FULL', 'name': 'Полная'}, 'internship': False, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None}]


@pytest.fixture
def vacancy_list():
    """Фикстура для создания списка объектов вакансий."""
    return [
        Vacancy("Python Developer", "Remote", 100000, "Company A", "http://example.com/1"),
        Vacancy("Java Developer", "Remote", 120000, "Company B", "http://example.com/2"),
        Vacancy("Data Scientist", "Remote", 110000, "Company C", "http://example.com/3"),
    ]