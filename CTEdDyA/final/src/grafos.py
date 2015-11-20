# -*- coding: utf-8 -*-


class Vertice(object):
    def __init__(self,dato, pos):
        self.__dato=dato
        self.__posicion=pos
        self.__adyacentes = []

    def getDato(self):
        return self.__dato

    def setDato (self,dato):
        self.__dato=dato

    def getPosicion(self):
        return self.__posicion

    def setPosicion(self,posicion):
        self.__posicion=posicion

    def getListaAdyacentes(self):
        return self.__adyacentes

    def __str__(self):
        return str(self.__dato)


class Arista(object):

    def __init__(self,peso,vertice):
        self.__verticeDestino=vertice
        self.__peso=peso

    def getVerticeDestino(self):
        return self.__verticeDestino

    def getPeso(self):
        return self.__peso


class Grafo(object):

    def __init__(self):
        self.__vetices=[]

    def agregarVertice(self, vertice):
        self.__vetices.append(vertice)

    def conectar(self, origen, destino, peso):
        origen.getListaAdyacentes().append(Arista(peso, destino))

    def getListaDeVertices(self):
        return self.__vetices

    def vertice(self, posicion):
        return self.__vetices[posicion]



