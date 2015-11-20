# -*- coding: utf-8 -*-

from src.listaenlazada import ListaConPyLista


class Cola(object):

    def __init__(self):
        self._datos = ListaConPyLista()

    def __str__(self):
        return str(self._datos)

    def __repr__(self):
        return self.__str__()

    def poner(self, elem):
        """ Agrega elem a la cola.
        Args:
            elem (Object): dato
        """
        self._datos.agregar(elem, 0)

    def sacar(self):
        """ Elimina y devuelve el elemento en el primer elemento de la cola.
        Returns:
            Object: primer elemento de la cola.
        """
        tamanio = self._datos.getTamanio()

        elem = self.tope()
        self._datos.eliminar(tamanio - 1)

        return elem

    def tope(self):
        """ Devuelve el primer elemento de la cola sin eliminarlo.
        Returns:
            Object: primer elemento de la cola.
        """
        tamanio = self._datos.getTamanio()
        elem = self._datos.elemento(tamanio -1)

        return elem

    def esVacia(self):
        """ Metodo para saber si la lista esta vacia o no.
        Returns:
            bool: True si la cola esta vacia y False si no lo esta.
        """
        return self._datos.esVacia()
