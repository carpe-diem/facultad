# -*- coding: utf-8 -*-
import abc
from abc import ABCMeta


class Recorredor(object):
    _actual = None

    __metaclass__ = ABCMeta

    def __init__(self, lista):
        self._lista = lista

    def comenzar(self):
        """Se prepara para recorrer los elementos de la lista."""
        if self._lista.getTamanio():
            self._actual = 0
        else:
            raise StopIteration("No hay elementos en la lista")

    def elemento(self):
        """ Retorna el elemento actual.
        Returns:
           Object: dato
        """
        try:
            nodo = self._lista._inicio

            count = 0

            while count != self._actual:
                nodo = nodo.getSiguiente()
                count += 1

            return nodo.getDato()

        except AttributeError:
            return self._lista._datos[self._actual]

        raise AttributeError

    def proximo(self):
        """ Avanza al próximo elemento de la lista."""

        if self._actual == self._lista.getTamanio():
            raise StopIteration("No hay más elementos en la lista")

        self._actual += 1

    def fin(self):
        """ Determina si llegó o no al final de la lista.
        Returns:
            bool: True si llefo al final y False si no llego.
        """
        if self._actual == self._lista.getTamanio():
            return True
        else:
            return False

    def agregar(self, elem):
        """ Agrega el elemento en la posición actual.
        Args:
            elem (Object): dato
        """
        self._lista.agregar(elem, self._actual)

    def eliminar(self):
        """ Elimina el elemento actual."""
        self._lista.eliminar(self._actual)
        self._actual -= 1


class Lista(object):
    """ Clase abstracta."""
    _tamanio = 0

    __metaclass__ = ABCMeta

    def recorredor(self):
        return Recorredor(self)

    def getTamanio(self):
        """ Metodo que devuelve la longitud de la lista.
        Returns:
            int: Tamaño de la lista
        """
        return self._tamanio

    @abc.abstractmethod
    def elemento(self, pos):
        raise NotImplementedError

    @abc.abstractmethod
    def agregar(self, elem, pos):
        raise NotImplementedError

    @abc.abstractmethod
    def eliminar(self, pos):
        raise NotImplementedError

    @abc.abstractmethod
    def esVacia(self):
        raise NotImplementedError

    @abc.abstractmethod
    def incluye(self, elem):
        raise NotImplementedError


class Nodo(object):
    _dato = None
    _siguiente = None

    def __str__(self):
        return u"Nodo <{d}>".format(d=self._dato)

    def __repr__(self):
        return self.__str__()

    def getDato(self):
        return self._dato

    def setDato(self, elem):
        self._dato = elem

    def getSiguiente(self):
        return self._siguiente

    def setSiguiente(self, sig):
        self._siguiente = sig


class ListaEnlazada(Lista):
    _inicio = None

    def __init__(self):
        Lista.__init__(self)

    def __str__(self):
        aux = self._inicio

        string = "["
        for n in range(0, self._tamanio):
            if n is not 0:
                string += ", "
            string += str(aux.getDato())
            aux = aux.getSiguiente()

        string += "]"

        return string

    def __repr__(self):
        return self.__str__()

    def elemento(self, pos):
        """ Retorna el elemento de la posición indicada.
        Args:
            pos (int): posición en la lista.
        Returns:
            Object: elemento del nodo.
        """
        if self._inicio == None or pos < 0 or pos > self._tamanio:
            raise IndexError

        aux = self._inicio
        count = 0

        while count != pos:
            aux = aux.getSiguiente()
            count += 1

        return aux.getDato()

    def agregar(self, elem, pos):
        """  Agrega el elemento en la posición indicada.
        Si no se pasa posición, lo agrega en la última.
        Args:
            elem (Object): dato
            pos (int): posición en la lista
        """
        if pos > self._tamanio or pos < 0:
            raise IndexError("Posición inválida")

        nuevo = Nodo()
        nuevo.setDato(elem)

        if self._inicio is None:
            self._inicio = nuevo
        elif self._inicio.getSiguiente() is None:
            self._inicio.setSiguiente(nuevo)
        elif pos == 0:
            nuevo.setSiguiente(self._inicio)
            self._inicio = nuevo
        else:
            actual = self._inicio
            count = 0
            while count != pos:
                siguiente = actual.getSiguiente()
                if count == pos - 1:
                    if siguiente is not None:
                        nuevo.setSiguiente(siguiente)
                    actual.setSiguiente(nuevo)

                actual = siguiente
                count += 1

        self._tamanio += 1

    def eliminar(self, pos):
        """ Elimina el elemento de la posición indicada.
        Args:
            pos (int): posición en la lista
        """

        if pos > self._tamanio - 1 or pos < 0:
            raise IndexError("Posición inválida")

        actual = self._inicio
        count = 0
        while count != pos + 1:
            siguiente = actual.getSiguiente()
            if pos == 0 and siguiente is None:
                self._inicio = None
            elif pos == 0 and siguiente is not  None:
                self._inicio = siguiente
            elif count == pos - 1:
                actual.setSiguiente(siguiente.getSiguiente())

            actual = siguiente
            count += 1

        self._tamanio -= 1

    def esVacia(self):
        """ Metodo para saber si la lista esta vacia o no.
        Returns:
            bool: True si la lista esta vacia y False si no lo esta.
        """
        return (self._tamanio == 0)

    def incluye(self, elem):
        """ Verificar si el elemento ya esta en la lista.
        Args:
            elem (Object): dato
        Returns:
            bool: True si elem esta contenido en la lista y False si no lo esta.
        """
        if self.esVacia():
            return False

        aux = self._inicio
        existe = False
        continuar = True

        while continuar:
            if aux.getDato() == elem:
                existe = True
                continuar = False
            aux = aux.getSiguiente()
            if aux is None:
                continuar = False

        return existe


class ListaConPyLista(Lista):

    def __init__(self):
        Lista.__init__(self)
        self._datos = []

    def __str__(self):
        return str(self._datos)

    def __repr__(self):
        return self.__str__()

    def elemento(self, pos):
        """ Retorna el elemento de la posición indicada.
        Args:
            pos (int): posición en la lista.
        Returns:
            Object: elemento del nodo.
        """
        if not self._datos or pos < 0 or pos > self._tamanio:
            raise IndexError

        return self._datos[pos]

    def agregar(self, elem, pos):
        """  Agrega el elemento en la posición indicada.
        Si no se pasa posición, lo agrega en la última.
        Args:
            elem (Object): dato
            pos (int): posición en la lista
        """
        if pos > self._tamanio or pos < 0:
            raise IndexError("Posición inválida")

        self._datos.insert(pos, elem)
        self._tamanio = len(self._datos)

    def eliminar(self, pos):
        """ Elimina el elemento de la posición indicada.
        Args:
            pos (int): posición en la lista
        """

        if pos > self._tamanio - 1 or pos < 0:
            raise IndexError("Posición inválida")

        self._datos.pop(pos)
        self._tamanio = len(self._datos)

    def esVacia(self):
        """ Metodo para saber si la lista esta vacia o no.
        Returns:
            bool: True si la lista esta vacia y False si no lo esta.
        """
        return (self._tamanio == 0)

    def incluye(self, elem):
        """ Verificar si el elemento ya esta en la lista.
        Args:
            elem (Object): dato
        Returns:
            bool: True si elem esta contenido en la lista y False si no lo esta.
        """
        return True if elem in self._datos else False

