from abc import ABCMeta, abstractmethod
import os
import xml.etree.ElementTree as ET



# абстрактный класс
class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}
    def add_param(self, key, value):
        self.params[key] = value
    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @staticmethod
    def get_instance(source):
        _, ext = os.path.splitext(str(source).lower())
        if ext == '.xml':
            return XmlParamHandler(source)
        return TextParamHandler(source)

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
            'Class "{}" is not ParamHandler!'.format(klass)
             )
        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):

        # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
          raise ParamHandlerException(
            'Type "{}" not found!'.format(ext)
            )
        return klass(source, *args, **kwargs)


class TextParamHandler(ParamHandler):
    def read(self):
        pass

    def write(self):
        f = open('params.txt', 'w')
        for keys, values in self.params.items():
            f.write(str(keys) + ' : ' + str(values) + '\n')

class XmlParamHandler(ParamHandler):
    def read(self):
        params = {}
        _, ext = os.path.split(str(self.source).lower())
        ext = ext[-3:]  # приводим к "xml"
        if ext == 'xml':
            tree = ET.ElementTree(file=self.source)
            root = tree.getroot()
            dimensions = root.findall('Dimension')  # Из тегов Dimension будем тащить атрибуты
            i = 0
            for dim in dimensions:  # Упарываемся с XML, будет уродливо
                # Добавляю в словарь элементы XML, атрибуты от Dimension
                params['Присутствует следующий разрез, внутренний индентификатор:' + str(i)] = dimensions[i].attrib
                i += 1
        else:
            raise TypeError(
                'Type "{}" is not supported for reading'.format(ext))

        return params
    def write(self):
        pass