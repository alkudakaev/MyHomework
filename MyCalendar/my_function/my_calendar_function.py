def choice_of_action(number):
    number = int(number)
    if number == 1:
        view_task_list()
    elif number == 2:
        add_new_task()
    elif number == 3:
        edit_task()
    elif number == 4:
        finish_task()
    elif number == 5:
        restart_task()
    elif number == 6:
        calendar_exit()


# 1. Вывести список задач
def view_task_list():
    print('Выводит список всех задач со статусом выполнения за указанный день')


# 2. Добавить задачу
def add_new_task():
    print('Добавить новую задачу')


# 3. Отредактировать задачу
def edit_task():
    print('Редактируем задачу по ID')


# 4. Завершить задачу
def finish_task():
    print('Меняет статус задачи на "Завершена"')


# 5. Начать задачу сначала
def restart_task():
    print('Меняет статус задачи на "Не выполнено"')


# 6. Выход
def calendar_exit():
    print('Выход из приложения ежедневника')
