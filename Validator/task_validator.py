from abc import ABCMeta, abstractmethod
from datetime import datetime
from string import digits


class ValidatorException(Exception):
    pass


class Validator(metaclass=ABCMeta):
    validators = {}

    @abstractmethod
    def validate(self):
        pass

    @classmethod
    def add_type(cls, name, validator):
        if not name:
            raise ValidatorException(
                'Validator must have a name!')
        if not issubclass(validator, cls):
            raise ValidatorException(
                'Class "{}" is not Validator!'.format(validator))
        cls.validators[name] = validator

    @classmethod
    def get_instance(cls, name):
        validator = cls.validators.get(name)

        if validator is None:
            raise ValidatorException(
                'Validator with name "{}" not found'.format(name))

        return validator


class EMailValidator(Validator):

    """

Немного изменил в этой части работу Евгения
Все имейлы имеют формат {адрес}@{доме.н}
Делим строку на части по @, получаем список.
Пытаемся всторой элемент списка разбить по точке, для проверки формата по точке {доме.н}


"""
    @staticmethod
    def validate(value):
        spt_adress = value.strip().split('@')
        try:
            dot_part = spt_adress[1].split('.') # делим второй элемент из списка spt_adress по точке,
        except:                                 # чтобы формат проверить
                return False
        if len(spt_adress) == 2 and len(dot_part) == 2:  # полученый список spt_adress
            return True                                 # должен состоять из двух элементов: {адрес} и {доме.н}
        else:                                          # dot_part также из двух {доме}{н}
            return False

class DateTimeValidator(Validator):
    validators = {
        '--': '%Y-%m-%d',
        '--:': '%Y-%m-%d %H:%M',
        '--::': '%Y-%m-%d %H:%M:%S',
        '..': '%d.%m.%Y',
        '..:': '%d.%m.%Y %H:%M',
        '..::': '%d.%m.%Y %H:%M:%S',
        '//': '%d/%m/%Y',
        '//:': '%d/%m/%Y %H:%M',
        '//::': '%d/%m/%Y %H:%M:%S',
    }


    @classmethod
    def validate(cls, value):
        fingerprint = ''.join(
            [x for x in value if x not in list(digits + ' ')]
        )
        validator = cls.validators.get(fingerprint)
        if  not validator:
            return False
        try:
            datetime.strptime(value, validator)
            return True
        except ValueError:
            return False


Validator.add_type('email', EMailValidator)
Validator.add_type('datetime', DateTimeValidator)


def main():
    validator = Validator.get_instance('email')
    print(validator.validate('a@ло.rгггг'))
    print(validator.validate('afdl.ru'))
    print(validator.validate('fdfs@fdfd@afdl.ru'))

    validator = Validator.get_instance('datetime')
    print(validator.validate('1.9.2017 12:00'))
    print(validator.validate('1/09/2017 12:04:10'))
    print(validator.validate('1.34.2017'))


if __name__ == '__main__':


    main()