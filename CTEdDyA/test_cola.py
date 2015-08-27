# -*- coding: utf-8 -*-
import unittest

from listaenlazada import ListaConPyLista
from cola import Cola


class Testcola(unittest.TestCase):

    def setUp(self):
        self.cola = Cola()
        self.d1 = 'dummy1'
        self.d2 = 'dummy2'
        self.d3 = 'dummy3'
        self.d4 = 'dummy4'

    def test_inicio(self):
        self.assertIsInstance(self.cola._datos, ListaConPyLista)

    def test_poner(self):
        self.cola.poner(self.d1)
        expected = str([self.d1])
        self.assertEqual(expected, str(self.cola))

        self.cola.poner(self.d2)
        expected = str([self.d2, self.d1])
        self.assertEqual(expected, str(self.cola))

        self.cola.poner(self.d3)
        expected = str([self.d3, self.d2, self.d1])
        self.assertEqual(expected, str(self.cola))

        self.cola.poner(self.d4)
        expected = str([self.d4, self.d3, self.d2, self.d1])
        self.assertEqual(expected, str(self.cola))

    def test_sacar(self):
        self.cola.poner(self.d1)
        self.cola.poner(self.d2)
        self.cola.poner(self.d3)
        self.cola.poner(self.d4)

        self.assertEqual(self.d1, self.cola.sacar())
        self.assertEqual(self.d2, self.cola.sacar())
        self.assertEqual(self.d3, self.cola.sacar())
        self.assertEqual(self.d4, self.cola.sacar())
        self.assertRaises(IndexError, self.cola.sacar)

    def test_tope(self):
        self.cola.poner(self.d1)
        self.assertEqual(self.d1, self.cola.tope())

        self.cola.poner(self.d2)
        self.assertEqual(self.d1, self.cola.tope())

        self.cola.poner(self.d3)
        self.assertEqual(self.d1, self.cola.tope())

        self.cola.poner(self.d4)
        self.assertEqual(self.d1, self.cola.tope())

    def test_EsVacia_si(self):
        self.assertTrue(self.cola.esVacia())

        self.cola.poner(self.d1)
        elem = self.cola.sacar()

        self.assertTrue(self.cola.esVacia())

    def test_EsVacia_no(self):
        self.cola.poner(self.d1)
        self.assertFalse(self.cola.esVacia())

        self.cola.poner(self.d2)
        self.assertFalse(self.cola.esVacia())

        elem = self.cola.sacar()
        self.assertFalse(self.cola.esVacia())


if __name__ == '__main__':
    unittest.main()
