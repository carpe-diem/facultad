# -*- coding: utf-8 -*-
import csv


class Ciudades(object):
    __FILE_CIUDADES = 'templates/ciudades.txt'
    __dict_ciudades = {}

    def __init__(self, file_ciudades=None):
        if file_ciudades is not None:
            self.__FILE_CIUDADES = file_ciudades
        self.__read_file()

    def __read_file(self):
        with open(self.__FILE_CIUDADES, 'r') as f:
            content = csv.reader(f, delimiter=',', quotechar='|')
            for index, data in enumerate(content):
                self.__dict_ciudades[index] = {
                    'nombre': data[0],
                    'usuarios': data[1],
                    'nivel_conexion': data[2],
                    'conectado_atyra': data[3],
                }

    def ciudades(cls):
        return cls.__dict_ciudades

