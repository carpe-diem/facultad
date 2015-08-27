# -*- coding: utf-8 -*-
import unittest

from listaenlazada import ListaConPyLista
from pila import Pila


class TestPila(unittest.TestCase):

    def setUp(self):
        self.pila = Pila()
        self.d1 = 'dummy1'
        self.d2 = 'dummy2'
        self.d3 = 'dummy3'
        self.d4 = 'dummy4'

    def test_inicio(self):
        self.assertIsInstance(self.pila._datos, ListaConPyLista)

    def test_poner(self):
        self.pila.poner(self.d1)
        expected = str([self.d1])
        self.assertEqual(expected, str(self.pila))

        self.pila.poner(self.d2)
        expected = str([self.d1, self.d2])
        self.assertEqual(expected, str(self.pila))

        self.pila.poner(self.d3)
        expected = str([self.d1, self.d2, self.d3])
        self.assertEqual(expected, str(self.pila))

        self.pila.poner(self.d4)
        expected = str([self.d1, self.d2, self.d3, self.d4])
        self.assertEqual(expected, str(self.pila))

    def test_sacar(self):
        self.pila.poner(self.d1)
        self.pila.poner(self.d2)
        self.pila.poner(self.d3)
        self.pila.poner(self.d4)

        self.assertEqual(self.d4, self.pila.sacar())
        self.assertEqual(self.d3, self.pila.sacar())
        self.assertEqual(self.d2, self.pila.sacar())
        self.assertEqual(self.d1, self.pila.sacar())
        self.assertRaises(IndexError, self.pila.sacar)

    def test_tope(self):
        self.pila.poner(self.d1)
        self.assertEqual(self.d1, self.pila.tope())

        self.pila.poner(self.d2)
        self.assertEqual(self.d2, self.pila.tope())

        self.pila.poner(self.d3)
        self.assertEqual(self.d3, self.pila.tope())

        self.pila.poner(self.d4)
        self.assertEqual(self.d4, self.pila.tope())

    def test_EsVacia_si(self):
        self.assertTrue(self.pila.esVacia())

        self.pila.poner(self.d1)
        elem = self.pila.sacar()

        self.assertTrue(self.pila.esVacia())

    def test_EsVacia_no(self):
        self.pila.poner(self.d1)
        self.assertFalse(self.pila.esVacia())

        self.pila.poner(self.d2)
        self.assertFalse(self.pila.esVacia())

        elem = self.pila.sacar()
        self.assertFalse(self.pila.esVacia())


if __name__ == '__main__':
    unittest.main()
