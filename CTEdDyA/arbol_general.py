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
        elif self._ArbolGeneral__getRaiz().getDato() == dato.getDato():
            return 0

        rec_hijos = self.getHijos().recorredor()
        try:
            rec_hijos.comenzar()
        except StopIteration:
            return -1

        nivel = -1
        counter = 1
#        nivel_count = 1
#        nivel_aux = 1
        listo = False
#
#        while not rec_hijos.fin() and not listo:
#            aux = rec_hijos.elemento().getDatoRaiz()
#
#            if aux != dato.getDato():
#                nivel_aux = rec_hijos.elemento().nivel(dato) + 1
#            else:
#                listo = True
#
#            rec_hijos.proximo()


        # Esto esta mal... terminar!
        while not rec_hijos.fin() and listo:
            aux = rec_hijos.elemento()
            if aux.getDato() == dato.getDato():
                nivel = counter
                listo = True
            else:
                aux = rec_hijos.elemento().nivel(dato)

            rec_hijos.proximo()


        return nivel

    def ancho(self):
        """ La amplitud (ancho) de un árbol se define como la
        cantidad de nodos que se encuentran en el nivel que posee
        la mayor cantidad de nodos.

        Returns:
            int: amplitud de un arbol.
        """
        pass

    def esAncestro(self, dato1, dato2):
        """ Determina si dato1 es ancestro de dato2.

        Args:
            dato1 (Object): dato
            dato2 (Object): dato

        Returns:
            bool: True si es ancestro, False si no lo es.
        """
        pass





