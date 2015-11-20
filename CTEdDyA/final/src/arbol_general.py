# -*- coding: utf-8 -*-

from listaenlazada import ListaConPyLista


class NodoGeneral(object):

    def __init__(self):
        self.__dato = None
        self.__trt = 0
        self.__listaHijos = ListaConPyLista()

    def __str__(self):
        return u"{d} ({l})".format(d=self.__dato,l=self.__trt)

    def __repr__(self):
        return self.__str__()

    def getDato(self):
        return self._NodoGeneral__dato

    def setDato(self, elem, trt):
        self._NodoGeneral__dato = elem
        self._NodoGeneral__trt = trt

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
        return self._ArbolGeneral__getRaiz()#.getDato()

    def getHijos(self):
        rec_hijos = self._ArbolGeneral__getRaiz().getHijos().recorredor()
        lista = ListaConPyLista()
        try:
            rec_hijos.comenzar()
        except StopIteration:
            return lista

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

    def altura(self):
        """ Devuelve la altura del árbol, la longitud del camino más
        largo desde el nodo raíz hasta una hoja.

        Returns:
            int: valor de la altura. (-1 si no tiene nodos).
        """
        if self._ArbolGeneral__getRaiz() is None:
            return -1

        rec_hijos = self.getHijos().recorredor()
        try:
            rec_hijos.comenzar()
        except StopIteration:
            return 0

        altura_max = 0

        while not rec_hijos.fin():
            aux = rec_hijos.elemento().altura() + 1
            if aux > altura_max:
                altura_max = aux
            rec_hijos.proximo()

        return altura_max

    def esHoja(self):
        return self.__raiz.getHijos() == []


    def nivel(self, dato):
        """ Devuelve la profundidad o nivel del dato en el árbol. 
        El nivel de un nodo es la longitud del único camino de la raíz al nodo.

        Args:
            dato (Object): dato

        Returns:
            int: profundidad
        """
        if self._ArbolGeneral__getRaiz() is None:
            return -1
        elif str(self._ArbolGeneral__getRaiz()) == str(dato):
            return 0



        rec_hijos = self.getHijos().recorredor()
        try:
            rec_hijos.comenzar()
        except StopIteration:
            return 0

        nivel = 1
        listo = False

        while not rec_hijos.fin():
            if rec_hijos.elemento().incluye(dato):
                nivel = rec_hijos.elemento().nivel(dato) + 1

            rec_hijos.proximo()

        return nivel

    def incluye(self, dato):
        if str(self._ArbolGeneral__getRaiz()) == str(dato):
            return True

        aux = False
        try:
            rec_hijos = self.getHijos().recorredor()
            rec_hijos.comenzar()
            while not rec_hijos.fin() and not aux:
                aux = rec_hijos.elemento().incluye(dato)
                rec_hijos.proximo()
        except:
            pass

        return aux
