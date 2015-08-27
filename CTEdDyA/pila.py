# -*- coding: utf-8 -*-

from listaenlazada import ListaConPyLista


class Pila(object):

    def __init__(self):
        self._datos = ListaConPyLista()

    def __str__(self):
        return str(self._datos)

    def __repr__(self):
        return self.__str__()

    def poner(self, elem):
        """ Agrega elem a la pila.
        Args:
            elem (Object): dato
        """
        tamanio = self._datos.getTamanio()
        self._datos.agregar(elem, tamanio)

    def sacar(self):
        """ Elimina y devuelve el elemento en el tope de la pila.
        Returns:
            Object: elemento en el tope de la lista.
        """
        tamanio = self._datos.getTamanio()

        elem = self.tope()
        self._datos.eliminar(tamanio - 1)

        return elem

    def tope(self):
        """ Devuelve el elemento en el tope de la pila sin eliminarlo.
        Returns:
            Object: elemento en el tope de la lista.
        """
        tamanio = self._datos.getTamanio()
        elem = self._datos.elemento(tamanio -1)

        return elem

    def esVacia(self):
        """ Metodo para saber si la lista esta vacia o no.
        Returns:
            bool: True si la pila esta vacia y False si no lo esta.
        """
        return self._datos.esVacia()
