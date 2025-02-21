from src.headhunter_api import HeadHunterAPI
from src.job_repository import JobRepository
from src.utils import top_vacancies, filter_by_words, filter_by_salary
from src.vacancy import Vacancy


def main():
    print('Поиск вакансий на платформе "HeadHunter"')
    hh_api = HeadHunterAPI()
    vacancy_holder = JobRepository()

    user_keyword = input('Введите поисковый запрос: ')
    vacancies_by_keyword = hh_api.get_vacancies(user_keyword)
    vacancies_object = Vacancy.create_obj_list(vacancies_by_keyword)
    top_n = int(input("Введите количество вакансий для вывода в топ N по зарплате: "))
    top_n_list = top_vacancies(vacancies_object, top_n)
    words_to_filter = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_list = filter_by_words(top_n_list, words_to_filter)
    salary_range = input("Введите диапазон зарплат (используйте формат: 'min - max'): ")
    result_list = filter_by_salary(filtered_list, salary_range)
    for res in result_list:
        print(res.vacancy_name)
    user_answer = input("Сохранить результаты в файл? (да, нет): ")
    if user_answer.lower() == "да":
        vacancy_holder.add_vacancies(result_list)
    while True:
        user_selection = input("Выберите следующее действие:\n"
                               "1 - Поиск вакансий\n"
                               "2 - Посмотреть сохраненный вакансии\n"
                               "3 - Удалить вакансии\n"
                               "4 - Выход из программы")

        if user_selection == '1':
            return main()
        elif user_selection == '2':
            vacancy_holder.read_vacancies()
        elif user_selection == '3':
            vacancy_holder.delete_vacancy()
        elif user_selection == '4':
            break
        else:
            print('Введите цифры от 1 до 4')




if __name__ == "__main__":
    main()
