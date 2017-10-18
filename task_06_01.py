import sys


def run_on_linux(func):
    def check_linux():
        f = sys.platform
        if f == 'linux':
            print('Функция выполняется только на Linux!')
            return func()
        else:
            return None
    return check_linux


def run_on_macos(func):
    def check_macos():
        f = sys.platform
        if f == 'macos':
            print('Функция выполняется только на Linux!')
            return func()
        else:
            return None
    return check_macos


def run_on_windows(func):
    def check_windows():
        f = sys.platform
        if f == 'windows':
            print('Функция выполняется только на Linux!')
            return func()
        else:
            return None
    return check_windows
