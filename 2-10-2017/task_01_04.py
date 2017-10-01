# Задача №4. Закрепляем математические операторы
# Напишите программу, предлагающую пользователю ввести три вершины.
# Координаты X и Y (2 числа), заданы как целые числа, т.е. int.
# Нужно определить является ли треугольник, с указанными координатами, прямоугольным.
# В решении использовать только математические и логические операторы.
# В вычислениях запрещено(!!!) переходить в дробные числа.
# Результат работы программы одно из слов:
# »> Прямоугольный
# »> Не прямоугольный
# Имя файла: task_01_04.py
# Входные данные: 2 7 6 1 12 5
# Выходные данные: Прямоугольный

print('Вам необходимо ввести координаты трёх вершин треугольника.\n'
      'Введите координаты первой точки по очереди, сначала X, потом Y:')
X1 = int(input())  # Будет вершиной А
Y1 = int(input())
print('Введите координаты второй точки по очереди, сначала X, потом Y:')
X2 = int(input())  # Будет вершиной В
Y2 = int(input())
print('Введите координаты третьей точки по очереди, сначала X, потом Y:')
X3 = int(input())  # Будет вершиной С
Y3 = int(input())

AB = int(((Y2-Y1)**2+(X2-X1)**2))
BC = int(((Y3-Y2)**2+(X3-X2)**2))
CA = int(((Y3-Y1)**2+(X3-X1)**2))

if AB == BC+CA:
    print('Прямоугольный')
elif BC == AB+CA:
    print('Прямоугольный')
elif CA == AB+BC:
    print('Прямоугольный')
else:
    print('Не прямоугольный')