# Задача №2.
# Реализуйте модуль number_system для перевода
# числа из одной системы счисления в другую.
# Модуль должен содержать 6 функций для перевода из десятичной системы счисления
#  в двоичную, восьмеричную, шестнадцатиричную и наоборот:
# - dec2bin(number) - возвращает str
# - dec2oct(number) - возвращает str
# - dec2hex(number) - возвращает str
# - bin2dec(number) - возвращает int
# - oct2dec(number) - возвращает int
# - hex2dec(number) - возвращает int
#
# (!) Запрещено использовать встроенные функции/методы, решающие эту задачу.
# Подсказка. Не спешите писать 6 разных реализаций, подумайте,
# можно ли написать универсальный алгоритм перевода.
# В решении не должно присутствовать операций ввода-вывода.
# Ситуации, когда в исходном числе есть не допустимые цифры (буквы), игнорируются.


def dec2bin(number):
    x = number
    n = ""
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    return n


def dec2oct(number):
    x = number
    n = ""
    while x > 0:
        y = str(x % 8)
        n = y + n
        x = int(x / 8)
    return n


def dec2hex(number):
    x = number
    hexarray = []
    while x > 0:
        y = str(x % 16)
        y = y.replace('10', 'A').replace('11', 'B').replace('12', 'C').replace('13', 'D').replace('14', 'E')\
            .replace('15', 'F')
        x = int(x / 16)
        hexarray.append(y)
    hexarray.reverse()
    answer = ''.join(hexarray)
    return answer


def bin2dec(number):
    a = str(number)
    b = a[::-1]
    y = 0
    i = 0
    while i < len(a):
        if b[i] == '1':
            n = 2 ** i
            y = y + n
        i = i + 1
    return y


def oct2dec(number):
    a = str(number)
    b = a[::-1]
    y = 0
    i = 0
    while i < len(a):
        n = int(b[i]) * (8 ** i)
        y = y + n
        i = i + 1
    return y


def hex2dec(number):
    a = str(number)
    b = a[::-1]
    y = 0
    i = 0
    while i < len(a):
        n = b[i]
        n = n.replace('A', '10').replace('B', '11').replace('C', '12').replace('D', '13').replace('E', '14') \
            .replace('F', '15')
        formula = int(n)*(16**i)
        y = y + formula
        i = i + 1
    return y
