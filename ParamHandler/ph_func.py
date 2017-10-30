# coding: utf-8
import os
import xml.etree.ElementTree as ET # https://docs.python.org/3/library/xml.etree.elementtr..



def read_params(source):
    params = {}
    shit_for_search = ['ObjectID',
                       'Process',
                       'Level',
                       'Filter/Dimension',
                       'Worksheets/Worksheet/DataAreas/DataArea/Head/Columns/Column/Dimension']
    """
    План следующий. Сделать список с полями, котороые меня инетерсуют.
    Через этото список выполнить поиск: 19.7.1.3. Finding interesting elements
    
    """
    _, ext = os.path.split(str(source).lower())
    ext = ext[-3:] # приводим к "xml"
    if ext == 'xml':
        tree = ET.ElementTree(file=source)
        root = tree.getroot()
        i = 0
        for element in shit_for_search:
            for root_part in root.findall(element):
                if not element.find('/') > 0:
                    # print('{}: {}'.format(root_part.tag, root_part.text))
                    params[root_part.tag] = root_part.text
                else:
                    # print('{}:{}'.format(element, root_part.attrib))
                    params[element+' '+str(i)] = root_part.attrib
                    i += 1
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
my_file_path = 'E:\\University\ITMO\MyHomework\ParamHandler\simple.xml'
my_path = 'E:\\University\ITMO\MyHomework\ParamHandler'
write_params(my_path,read_params(my_file_path))



