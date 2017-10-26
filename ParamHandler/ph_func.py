# coding: utf-8
import os
import xml.etree.ElementTree as ET # https://docs.python.org/3/library/xml.etree.elementtr..
# Упарываемся с XML

def read_params(source):
    params = {}
    _, ext = os.path.split(str(source).lower())
    ext = ext[-3:]
    if ext == 'xml':
        tree = ET.ElementTree(file=source)
        root = tree.getroot()
        for child_of_root in root.iter():
            params[child_of_root.tag] = child_of_root.text
    else:
        raise TypeError(
            'Type "{}" is not supported for reading'.format(ext))
    return params


def write_params(source, params):
    pass