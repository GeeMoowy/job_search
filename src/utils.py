

def filter_by_words(vacancy_list, words_to_filter):
    """Функция фильтрации списка вакансий по заданным ключевым словам"""
    if len(words_to_filter) == 0:
        return vacancy_list
    else:
        filtered_vacancies = []
        for vacancy in vacancy_list:
            # Проверяем, содержится ли хотя бы одно из ключевых слов в названии вакансии
            if any(keyword in vacancy.vacancy_name.lower() for keyword in words_to_filter):
                filtered_vacancies.append(vacancy)
        if len(filtered_vacancies) == 0:
            raise ValueError('Совпадения по ключевым слова не найдены')
        return filtered_vacancies


def top_vacancies(vacancies, top_n):
    """Выводит топ N вакансий по зарплате."""
    # Сортируем вакансии по зарплате в порядке убывания
    sorted_vacancies = sorted(vacancies, key=lambda v: v.salary_from, reverse=True)

    # Берем только топ N вакансий
    top_vacancies = sorted_vacancies[:top_n]

    # Выводим информацию о топ N вакансиях
    for vacancy in top_vacancies:
        print(
            f"Название: {vacancy.vacancy_name}, Зарплата: {vacancy.salary_from}, "
            f"Работодатель: {vacancy.employer}, Ссылка: {vacancy.url}")
    return top_vacancies


def filter_by_salary(vacancy_list, salary_range):
    """Фильтрует вакансии по заданному диапазону зарплат."""
    # Разделяем диапазон на минимальную и максимальную зарплату
    try:
        min_salary, max_salary = map(int, salary_range.split('-'))
    except ValueError:
        print("Неверный формат диапазона. Пожалуйста, используйте формат: 'min - max'.")
        return []

    filtered_vacancies = []
    for vacancy in vacancy_list:
        if min_salary <= vacancy.salary_from <= max_salary:
            filtered_vacancies.append(vacancy)
    return filtered_vacancies