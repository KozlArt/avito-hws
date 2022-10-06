from typing import Dict
from statistics import mean


def read_csv(filepath: str, sep: str = ";") -> Dict:
    """
    Считывает csv файл и возвращает словарь с ключами - заголовками csv и значениями - столбцами
    :param filepath: путь до файла
    :param sep: разделитель в csv файле
    :return: словарь с ключами - заголовками csv и значениями - столбцами
    """
    with open(filepath, 'r') as file:
        lines = file.read().split("\n")
    for i, elm in enumerate(lines):
        lines[i] = elm.split(sep)
    res_dict = {}
    for i in lines[0]:
        res_dict[i] = []

    # здесь все таки нужен range(len()) потому что идет "переворачивание индексов"
    for i in range(1, len(lines) - 1):
        for j, elm in enumerate(lines[0]):
            res_dict[elm].append(lines[i][j])
    return res_dict


def save_csv(filedict: Dict, filepath: str, sep: str = ";") -> None:
    """
    Сохраняет словарь в csv файл, используя ключи как заголовки столбцов
    :param filedict: словарь данных
    :param filepath: путь сохранения csv
    :param sep: разделитель csv
    """
    res_file = sep.join([i for i in filedict]) + "\n"
    res_list = [filedict[i] for i in filedict]

    # здесь все таки нужен range(len()) потому что идет "переворачивание индексов"
    for i in range(len(res_list[0])):
        line = []
        for j in range(len(filedict)):
            line.append(res_list[j][i])
        res_file = res_file + sep.join(line) + "\n"

    with open(filepath, 'w') as file:
        file.write(res_file)



def hierarchy(filedict: Dict, department: str = "Департамент", division: str = "Отдел") -> None:
    """
    Выводит иерархию Департамент - отдел
    :param filedict: словарь данных
    :param department: название ключа департамента
    :param division: название ключа отдела
    """
    department = filedict[department]
    division = filedict[division]
    departments = {}
    for i in set(department):
        departments[i] = []

    for i, elm in enumerate(department):
        departments[elm].append(division[i])

    for i in departments:
        departments[i] = list(set(departments[i]))

    print('------------------------------')
    print('Список Департаментов и Отделов')
    print('------------------------------')
    for i in departments:
        print(i, ':', ', '.join(departments[i]))
    print('------------------------------')


def cons_report(filedict: Dict, department: str = 'Департамент', payment: str = 'Оклад', verbose: bool = True) -> Dict:
    """
    сводный отчёт по департаментам: название, численность, мин, макс, среднюю зарплату
    :param filedict: словарь данных
    :param department: название ключа департамента
    :param payment: название ключа зарплаты
    :param verbose: если True - выводит в отчет в командную строку, False - не выводит
    :return: словарь сводного очета для последующего сохранения save_csv()
    """
    department = filedict[department]
    payment = filedict[payment]
    departments = {}
    for i in set(department):
        departments[i] = []

    for i, elm in enumerate(department):
        departments[elm].append(int(payment[i]))

    for i in departments:
        departments[i] = [str(i) for i in
                          [len(departments[i]), min(departments[i]), max(departments[i]), int(mean(departments[i]))]]
    if verbose:
        print('-----------------------------------')
        print('Сводная статистика по Департаментам')
        print('-----------------------------------')
        print('Название : количество - мин зп - макс зп - средняя зп')
        for i in departments:
            print(i, ':', ' - '.join(departments[i]))
        print('-----------------------------------')

    res_dict = {}
    res_dict['Департамент'] = [i for i in departments]
    res_dict['Количество сотрудников'] = [departments[i][0] for i in departments]
    res_dict['Минимальный оклад'] = [departments[i][1] for i in departments]
    res_dict['Максимальный оклад'] = [departments[i][2] for i in departments]
    res_dict['Средний оклад'] = [departments[i][3] for i in departments]
    return res_dict


def menu() -> None:
    """
    Меню для управления программой через командную строку
    """
    filepath = input("Введите путь до файла: ")
    data = read_csv(filepath)
    print("""Введите команду числом:
            1. Вывести все департаменты и их отделы.
            2. Сформировать сводный отчет - количество работников в департаменте,
                                            минимальный, максимальный и средний оклад.
            3. Сохранить сводный отчет в файл.
            4. Выйти из программы.
    """)
    report_flag = False
    while True:
        answers = ['1', '2', '3', '4']
        answer = '0'
        while answer not in answers:
            answer = input('Введите номер команды:')

        if answer == '1':
            hierarchy(data)
        elif answer == '2':
            report = cons_report(data)
            report_flag = True
        elif answer == '3':
            filepath = input('Введите путь для сохранения: ')
            if report_flag:
                save_csv(report, filepath)
            else:
                report = cons_report(data, verbose=False)
                save_csv(report, filepath)
        elif answer == '4':
            return


if __name__ == '__main__':
    # ./data/Corp_Summary.csv
    menu()
