import sys
import os.path as Path
from my_function import storage
get_connection = lambda: storage.connect('calendar.sqlite')


def action_show_menu():
    """показать меню"""
    print("""Ежедневник, выберите действие:
      1. Вывести список задач
      2. Добавить задачу
      3. Отредактировать задачу
      4. Завершить задачу
      5. Начать задачу сначала
      6. Выход
      7. Вывести всё""")


def main():
    creation_schema = Path.join(
        Path.dirname(__file__), 'schema.sql'  # __file__ абсолютный путь к текущему модулю
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': view_task_list,
        '2': add_new_task,
        '3': edit_task,
        '4': finish_task,
        '5': restart_task,
        '6': calendar_exit,
        '7': select_all
    }
    action_show_menu()

    while 1:
        cmd = input('\n Введите команду:')
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Неизвестная команада')


# 1. Вывести список невыполненых задач за определённый день
def view_task_list():
    execution_date = input('Введите дату выполнения задачи, формат ГГГГ-ММ-ДД:\n')
    status = input('Введите интересующий вас статус 1 - Выполнено, 0 - Не выполнено:\n')
    with get_connection() as conn:
        rows = storage.find_active_task_on_day(conn, status, execution_date)
    template = '{row[ObjectId]} - {row[Name]}'
    for row in rows:
        print('Вот:' + template.format(row=row))


# 2. Добавить задачу
def add_new_task():
    name = input('Введите название задачи:\n')
    description = input('Введите описание задачи:\n')
    status = input('Введите статус задачи, 1 - Выполнено, 0 - Не выполнено:\n')
    execution_date = input('Введите дату выполнения задачи, формат ГГГГ-ММ-ДД:\n')

    with get_connection() as conn:
        new_task = storage.add_task(conn, name, description, status, execution_date)

    print('Добавлена задача: ' + new_task)


# 3. Отредактировать задачу
def edit_task():
    object_id = input('Введите ID задачи:\n')
    name = input('Введите новое название задачи:\n')
    description = input('Введите новое описание задачи:\n')
    status = input('Введите новый статус задачи, 1 - Выполнено, 0 - Не выполнено:\n')
    execution_date = input('Введите новую дату выполнения задачи, формат ГГГГ-ММ-ДД:\n')

    with get_connection() as conn:
        storage.update_task_by_id(conn, object_id, name, description, status, execution_date)

    print('Задача с ID ' + object_id + 'обновлена')


# 4. Завершить задачу
def finish_task():
    print('Меняет статус задачи на "Завершена" - 1')
    status = 1
    object_id = input('Введите ID задачи:\n')
    with get_connection() as conn:
        storage.change_status(conn, status, object_id)


# 5. Начать задачу сначала
def restart_task():
    print('Меняет статус задачи на "Не завершена" - 0')
    status = 0
    object_id = input('Введите ID задачи:\n')
    with get_connection() as conn:
        storage.change_status(conn, status, object_id)


# 6. Выход
def calendar_exit():
    print('Выход из приложения ежедневника')
    sys.exit(0)


# 7. вывести список всех задач
def select_all():
    with get_connection() as conn:
        rows = storage.select_all(conn)
    template = '{row[Name]} - {row[Status]} - {row[ExecutionDate]}'
    for row in rows:
        print(template.format(row=row))
