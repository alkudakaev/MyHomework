# Задача №1
# Попробуйте перенести в ОО-код следующий пример из реального мира:
# - есть курсы, учителя и ученики
# - у каждого курса есть свой учитель
# - у каждого учителя есть своя группа учеников
# - у каждого ученика есть свой учитель
# и т.д.


class Person(object): # Персона, сопрём из классной работы и возмём за основу
    def __init__(self, firstname1, lastname2, document3, contacts4):
        """
        Метод-конструктор
        Основая цель конструктора
            - инициализировать объект!

        self - ссылка на текущий экземпляр (объект)
        """
        print(firstname1)
        self.firstname = firstname1 + 'тесттест'
        self.lastname = lastname2
        self.document = document3
        self.contacts = contacts4
        print(self.firstname + 'это селф')

    def print_info(self):
        print('{} {}'.format(self.firstname,
                             self.lastname))


ddd = Person('1111', '22323', '23423', '234234')

# ivan = Person('Ivan','Ivanov', '89219781433', 'Severnaya str')
# print(ivan.print_info())

# class Teacher(Person): #Создадим класс учителя
#     def __init__(self, firstname, lastname, document, contacts, grade, subject): # иницируем параметры(аргументы?)
#                                                                                                 # grade - должность subject - предмет
#         super().__init__(firstname, lastname, document, contacts)
#         self.grade = grade
#         self.subject = subject
#         self.group = None
#
#     def get_info(self):
#         print('The teacher {} {}, subject: {} , contacts: {}, leads a group: {}'.format(self.firstname, self.lastname,
#                                                                                         self.subject, self.contacts,
#                                                                                         self.group))
#
#     def set_group(self, group):
#         self.group = group
#         print('The teacher {} {} now oversees the group {}'.format(self.firstname, self.lastname,self.group))
#
#     def update_all(self, firstname, lastname, document, contacts, grade, subject, group):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.document = document
#         self.contacts = contacts
#         self.grade = grade
#         self.subject = subject
#         self.group = group
#
#
# class Student(Person):
#     def __init__(self, firstname, lastname, document, contacts, group, teacher):
#         super().__init__(firstname, lastname, document, contacts)
#         self.group = group
#         self.teacher = teacher
#
#     def get_name(self):
#         return self.firstname + ' ' + self.lastname
#
#     def get_info(self):
#         print('The student {} {}, contacts: {}, study in a group: {}'.format(self.firstname, self.lastname,
#                                                                              self.contacts, self.group))
#
#     def set_group(self, group):
#         self.group = group
#         print('The student {} {} transferred to the group: {}'.format(self.firstname, self.lastname,
#                                                                              self.group))
#
#     def update_all(self, firstname, lastname, document, contacts, group, teacher):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.document = document
#         self.contacts = contacts
#         self.group = group
#         self.teacher = teacher
#
#
# class Group(object):
#     def __init__(self, codename, description, teacher):
#         self.codename = codename
#         self.list = []
#         self.description = description
#         self.teacher = teacher
#
#     def get_info(self):
#         print('Group {}, {}'.format(self.codename, self.description))
#
#     def get_list_of_group(self,):
#         print(self.list, sep='\n')
#
#     def add_student(self, student):
#         self.list.append(student)
#
#     def remove_student(self, student):
#         self.list.remove(student)
#
#     def update_all(self, codename, description, teacher):
#         self.codename = codename
#         self.list = []
#         self.description = description
#         self.teacher = teacher
#
#     def get_codename(self):
#         return self.codename
#
#
# prepod = Teacher('Ivan', 'Ivanov', 'Passport:9999', '89219781433', 'Prof.', 'Math')
# first_group = Group(42,'test group', prepod)
# student1 = Student('Alex', 'Pros', 'Passport: 01233', 'dfdfdf', first_group, prepod)
# student2 = Student('Den', 'Prostodenov', 'Passport: 000033', 'alkudakaev@yandex.ru', first_group, prepod)
# first_group.add_student(student1.get_name())
# first_group.add_student(student2.get_name())
# prepod.set_group(first_group.get_codename())
#
# print(prepod.get_info())
#
#
