from abc import ABCMeta, abstractmethod
import os
import xml.etree.ElementTree as ET


class ParamHandlerException(Exception):
 pass


class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def insert_param(self,value):
        self.params=value

    def get_all_params(self):
        return self.params

    def get_source(self):
        return str(self.source)

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    types = {}


    @classmethod
    def add_type(cls, name, clas):
        if not name:
            raise ParamHandlerException('Type must have a name!')

        if not issubclass(clas, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(clas))
        cls.types[name] = clas

    @classmethod
    def get_instance(cls, source, *args, **kwargs):

         # Шаблон "Factory Method"
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        clas = cls.types.get(ext)
        if clas is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))

        return cls(source, *args, **kwargs)



class XmlParamHandler(ParamHandler):
    def __init__(self, source):
        super().__init__(source)
        self.shit_for_search = ['ObjectID', # будем дополнять по аналогии с types из ParamHandler
                       'Process',
                       'Level',
                       'Filter/Dimension',
                       'Worksheets/Worksheet/DataAreas/DataArea/Head/Columns/Column/Dimension']

    def read_params(self):
        params = {}
        _, ext = os.path.split(str(self.source).lower())
        ext = ext[-3:]  # приводим к "xml"
        if ext == 'xml':
            tree = ET.ElementTree(file=self.source)
            root = tree.getroot()
            i = 0
            for element in self.shit_for_search:
                for root_part in root.findall(element):
                    if not element.find('/') > 0: # если есть в элементе слеш, то искать надо по атрибуту
                        # print('{}: {}'.format(root_part.tag, root_part.text))
                        params[root_part.tag] = root_part.text
                    else:
                        # print('{}:{}'.format(element, root_part.attrib))
                        params[element + ' ' + str(i)] = root_part.attrib
                        i += 1
        else:
            raise TypeError(
                'Type "{}" is not supported for reading'.format(ext))

        return params

    def add_element_for_search(self, string):
        self.shit_for_search.append(string)

    def read(self):
        with open(self.get_source(), 'r') as f:
            a = self.read_params()
            self.insert_param(a)

    def write(self):
        with open(self.get_source(), 'r') as f:
            for keys, values in self.params.items():
                f.write(str(keys) + ' : ' + str(values) + '\n')


