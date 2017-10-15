import os.path as Path
import sqlite3

SQL_SELECT_ALL = """
SELECT ObjectId, Name, Status, Description, CreateDate, ExecutionDate
FROM calendar
"""
# Запрашиваем дату по определённому статусу + дате
SQL_SELECT_TASKS_BY_STATUS_AND_DAY = SQL_SELECT_ALL + " WHERE Status = ? AND ExecutionDate = ?"

# Добавить задачу
SQL_INSERT_TASK = """INSERT INTO calendar (Name, Status, Description, ExecutionDate) VALUES (?, ?, ?, ?)"""

# Обновить задачу по ИД
SQL_UPDATE_TASK_BY_ID = """UPDATE calendar SET Name = ?, Status = ?, Description = ?, 
ExecutionDate = ? WHERE ObjectId = ?"""

# Завершить задачу. Меняет статус задачи на "Выполнено"/"Не выполнено"
SQL_UPDATE_STATUS = """UPDATE calendar SET Status = ? WHERE ObjectID = ?"""


def dict_factory(cursor, row):
    d = {}
    print('==>> Row', row)
    print('==>>', cursor.description)

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn


def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f:
        conn.executescript(f.read())

# Добавим новую задачу


def add_task(conn, name, status, description, execution_date):
    """Сохраняет новую задачу в базу"""
    with conn:
            conn.execute(SQL_INSERT_TASK, (name, status, description, execution_date,))
    return name


def find_active_task_on_day(conn, status, execution_day):
    """Возвращает ULR-адрес по оригинальному адресу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_TASKS_BY_STATUS_AND_DAY, (status, execution_day,))
    return cursor.fetchall()


def update_task_by_id(conn, object_id, name, description, status, execution_date):
    """Возвращает ULR-адрес по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_UPDATE_TASK_BY_ID, (name, description, status, execution_date, object_id))
    return cursor.fetchall()


def change_status(conn, status, object_id):
    """Возвращает ULR-адрес по первичному короткому адресу"""
    with conn:
        cursor = conn.execute(SQL_UPDATE_STATUS, (status, object_id))
    return cursor.fetchall()


def select_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL)
    return cursor.fetchall()
