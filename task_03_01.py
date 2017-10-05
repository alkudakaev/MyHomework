# Задача №1.
# Напишите функцию get_days_to_new_year,
# которая возвращает количество дней, оставшихся до нового года.
# Датой наступления нового года считается 1 января.
# Функция должна корректно работать при запуске в любом году,
# т. е. грядущий год должен вычисляться программно.
# Для решения задачи понадобится стандартный модуль datetime
# https://docs.python.org/3/library/datetime.html
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.
# Имя файла: task_03_01.py
# Имя функции: get_days_to_new_year
# Возвращаемое значение: int


def get_days_to_new_year():
    import datetime
    now = datetime.date.today()  # забрали дату
    new_year_date = datetime.date((int(now.strftime('%Y')) + 1), 1, 1)  # привели к виду (текущий год+1)-01-01
    count_of_days = new_year_date - now  # количество дней в формате дельты
    count_of_days = int(count_of_days.days)
    print(count_of_days)
