# coding: utf-8
import os
import xml.etree.ElementTree as ET # https://docs.python.org/3/library/xml.etree.elementtr..



def read_params(source):
    params = {}
    shit_for_search = ['ObjectID', 'Process', 'Level', 'Filter/Dimension', 'Column/Dimension']
    """
    План следующий. Сделать список с полями, котороые меня инетерсуют.
    Через этото список выполнить поиск: 19.7.1.3. Finding interesting elements
    
    """
    _, ext = os.path.split(str(source).lower())
    ext = ext[-3:] # приводим к "xml"
    if ext == 'xml':
        tree = ET.ElementTree(file=source)
        root = tree.getroot()
        for element in shit_for_search:
            for root_part in root.findall(element):
                print('{} {}'.format(root_part.tag, root_part.text))
                print(root_part.attrib)

        """
        
        Старый код, он не подходит под задачу перевода в ООП
        
        # dimensions = root.findall('Dimension') # Из тегов Dimension будем тащить атрибуты
        # i = 0
        # for dim in dimensions:  # Упарываемся с XML, будет уродливо
        #     # Добавляю в словарь элементы XML, атрибуты от Dimension
        #     params['Присутствует следующий разрез, внутренний индентификатор:'+str(i)] = dimensions[i].attrib
        #     i += 1
        """
    else:
        raise TypeError(
            'Type "{}" is not supported for reading'.format(ext))

    return params

# сделано без проверок, запись полученого конфига будет вестись в txt
def write_params(source, params):
    f = open('params_new.txt', 'w')
    for keys, values in params.items():
        f.write(str(keys)+' : '+str(values)+'\n')


# Тут надо свой путь прописать
my_file_path = '/home/akudakaev/python-2017-3/MyHomework/MyHomework/ParamHandler/simple.xml'
my_path = '/home/akudakaev/python-2017-3/MyHomework/MyHomework/ParamHandler/'
write_params(my_path,read_params(my_file_path))



