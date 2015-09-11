# -*- coding: utf-8 -*-

from listaenlazada import ListaConPyLista


class NodoGeneral(object):

    def __init__(self):
        self.__dato = None
        self.__listaHijos = ListaConPyLista()

    def __str__(self):
        return u"Nodo <{d}: {l}>".format(d=self.__dato,
            l=self._NodoGeneral__listaHijos)

    def __repr__(self):
        return self.__str__()

    def getDato(self):
        return self._NodoGeneral__dato

    def setDato(self, elem):
        self._NodoGeneral__dato = elem

    def getHijos(self):
        return self._NodoGeneral__listaHijos

    def setHijos(self, hijos):
        self._NodoGeneral__listaHijos = hijos


class ArbolGeneral(object):

    def __init__(self, raiz=None):
        self.__raiz = raiz

    def __str__(self):
        return u"{d}".format(d=self.__raiz)

    def __repr__(self):
        return self.__str__()

    def __getRaiz(self):
        return self.__raiz

    def __setRaiz(self, raiz):
        self.__raiz = raiz

    def getDatoRaiz(self):
        return self._ArbolGeneral__getRaiz().getDato()

    def getHijos(self):
        rec_hijos = self._ArbolGeneral__getRaiz().getHijos().recorredor()
        lista = ListaConPyLista()
        rec_hijos.comenzar()

        while not rec_hijos.fin():
            arbol = ArbolGeneral(rec_hijos.elemento())
            lista.agregar(arbol, lista.getTamanio())
            rec_hijos.proximo()

        return lista

    def agregarHijo(self, hijo):
        nodo_raiz = self._ArbolGeneral__getRaiz()
        lista = nodo_raiz.getHijos()
        lista.agregar(hijo, lista.getTamanio())

    def eliminarHijo(self, hijo):
        nodo_raiz = self._ArbolGeneral__getRaiz()
        rec_lista = nodo_raiz.getHijos().recorredor()
        rec_lista.comenzar()

        borrado = False

        while not rec_lista.fin() or not borrado:
            if rec_lista.elemento().getDato() == hijo.getDato():
                rec_lista.eliminar()
                borrado = True

            rec_lista.proximo()




