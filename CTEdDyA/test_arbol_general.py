# -*- coding: utf-8 -*-
import unittest

from listaenlazada import ListaConPyLista
from arbol_general import NodoGeneral, ArbolGeneral


class TestNodoGeneral(unittest.TestCase):

    def setUp(self):
        self.DUMMY_0 = 'dummy0'
        self.DUMMY_1 = 'dummy1'
        self.DUMMY_2 = 'dummy2'
        self.DUMMY_3 = 'dummy3'
        self.nodo_general = NodoGeneral()

    def test_inicio(self):
        self.assertEqual(None, self.nodo_general._NodoGeneral__dato)
        self.assertIsInstance(self.nodo_general._NodoGeneral__listaHijos, ListaConPyLista)

    def test_get_dato(self):
        self.nodo_general._NodoGeneral__dato = self.DUMMY_0
        self.assertEqual(self.DUMMY_0, self.nodo_general.getDato())

    def test_set_dato(self):
        self.nodo_general.setDato(self.DUMMY_1)
        self.assertEqual(self.DUMMY_1, self.nodo_general.getDato())

    def test_get_hijos(self):
        self.nodo_general.setDato("dummy_nodo_1")
        lista = ListaConPyLista()
        lista.agregar(self.DUMMY_0, 0)
        lista.agregar(self.DUMMY_1, 1)
        lista.agregar(self.DUMMY_2, 2)
        lista.agregar(self.DUMMY_3, 2)
        self.nodo_general._NodoGeneral__listaHijos = lista

        self.assertEqual(lista, self.nodo_general.getHijos())

    def test_set_hijos(self):
        lista = ListaConPyLista()
        lista.agregar(self.DUMMY_0, 0)
        lista.agregar(self.DUMMY_1, 1)
        lista.agregar(self.DUMMY_2, 2)
        lista.agregar(self.DUMMY_3, 2)

        self.nodo_general.setHijos(lista)

        self.assertEqual(lista, self.nodo_general._NodoGeneral__listaHijos)


class TestArbolGeneral(unittest.TestCase):

    def setUp(self):
        #self.DUMMY_0 = 'dummy0'
        #self.DUMMY_1 = 'dummy1'
        #self.DUMMY_2 = 'dummy2'
        #self.DUMMY_3 = 'dummy3'

        #self.lista = ListaConPyLista()
        #self.lista.agregar(self.DUMMY_0, 0)
        #self.lista.agregar(self.DUMMY_1, 1)
        #self.lista.agregar(self.DUMMY_2, 2)
        #self.lista.agregar(self.DUMMY_3, 2)

        #self.nodo_general = NodoGeneral()
        #self.nodo_general.setDato(self.DUMMY_0)
        #self.nodo_general.setHijos(self.lista)

        """
                        1
                        |
                   ----- -----
                  |           |
                  2           3
                  |           |
                -- --       -- --
               |     |     |     |
               4     5     6     7

        """
        self.ng7 = NodoGeneral()
        self.ng6 = NodoGeneral()
        self.ng5 = NodoGeneral()
        self.ng4 = NodoGeneral()
        self.ng2 = NodoGeneral()
        self.ng3 = NodoGeneral()
        self.ng1 = NodoGeneral()

        self.ng7._NodoGeneral__dato = 7
        self.ng6._NodoGeneral__dato = 6
        self.ng5._NodoGeneral__dato = 5
        self.ng4._NodoGeneral__dato = 4
        self.ng3._NodoGeneral__dato = 3
        self.ng2._NodoGeneral__dato = 2
        self.ng1._NodoGeneral__dato = 1

        self.l1 = ListaConPyLista()
        self.l2 = ListaConPyLista()
        self.l3 = ListaConPyLista()
        self.l4 = ListaConPyLista()
        self.l5 = ListaConPyLista()
        self.l6 = ListaConPyLista()
        self.l7 = ListaConPyLista()

        self.ag1 = ArbolGeneral()
        self.ag2 = ArbolGeneral()
        self.ag3 = ArbolGeneral()
        self.ag4 = ArbolGeneral()
        self.ag5 = ArbolGeneral()
        self.ag6 = ArbolGeneral()
        self.ag7 = ArbolGeneral()

        self.l3.agregar(self.ng6, 0)
        self.l3.agregar(self.ng7, 1)
        self.ng3._NodoGeneral__listaHijos = self.l3

        self.l2.agregar(self.ng4, 0)
        self.l2.agregar(self.ng5, 1)
        self.ng2._NodoGeneral__listaHijos = self.l2

        self.l1.agregar(self.ng2, 0)
        self.l1.agregar(self.ng3, 1)
        self.ng1._NodoGeneral__listaHijos = self.l1

        self.arbol_general = ArbolGeneral()
        self.arbol_general._ArbolGeneral__raiz = self.ng1


    def test_inicio(self):
        ag = ArbolGeneral()
        self.assertEqual(None, ag._ArbolGeneral__raiz)

    def test_get_raiz(self):
        self.assertEqual(self.ng1, self.arbol_general._ArbolGeneral__getRaiz())

    def test_set_raiz(self):
        self.arbol_general._ArbolGeneral__setRaiz(self.ng1)
        self.assertEqual(self.ng1,
            self.arbol_general._ArbolGeneral__raiz)

    def test_get_dato_raiz(self):
        self.arbol_general._ArbolGeneral__raiz = self.ng1
        self.assertEqual(1, self.arbol_general.getDatoRaiz())

    def test_get_hijos(self):
        self.assertEqual(str(self.l1), str(self.arbol_general.getHijos()))

    def test_get_hijos_none(self):
        arbol_dummy = ArbolGeneral()
        arbol_dummy._ArbolGeneral__raiz = self.ng7

        self.assertEqual(str(ListaConPyLista()), str(arbol_dummy.getHijos()))

    def test_agregar_hijo(self):
        ng_nuevo = NodoGeneral()
        l_nuevo = ListaConPyLista()
        ng_nuevo._NodoGeneral__listaHijos = l_nuevo
        ng_nuevo._NodoGeneral__dato = 8

        self.arbol_general.agregarHijo(ng_nuevo)

        self.l1.agregar(ng_nuevo, 2)
        self.assertEqual(str(self.l1), str(self.arbol_general.getHijos()))

    def test_eliminar_hijo(self):
        self.arbol_general.eliminarHijo(self.ng2)

        lista = ListaConPyLista()
        lista.agregar(self.ng3, 0)

        self.assertEqual(str(lista), str(self.arbol_general.getHijos()))
        self.arbol_general.eliminarHijo(self.ng3)

        # No hay mas hijos
        self.assertRaises(StopIteration,
            self.arbol_general.eliminarHijo, self.ng3)

    def test_altura_sin_datos(self):
        arbol_dummy = ArbolGeneral()
        self.assertEqual(-1, arbol_dummy.altura())

    def test_altura_cero(self):
        arbol_dummy = ArbolGeneral()
        arbol_dummy._ArbolGeneral__raiz = self.ng7

        self.assertEqual(0, arbol_dummy.altura())

    def test_altura_mayor_0(self):
        arbol_dummy2 = ArbolGeneral()
        arbol_dummy2._ArbolGeneral__raiz = self.ng2
        self.assertEqual(1, arbol_dummy2.altura())

        arbol_dummy3 = ArbolGeneral()
        arbol_dummy3._ArbolGeneral__raiz = self.ng2
        self.assertEqual(1, arbol_dummy3.altura())

        self.assertEqual(2, self.arbol_general.altura())

    def test_nivel_sin_datos(self):
        arbol_dummy = ArbolGeneral()
        self.assertEqual(-1, arbol_dummy.nivel(self.ng1))

    def test_nivel_dato_no_existe(self):
        ng_nuevo = NodoGeneral()
        l_nuevo = ListaConPyLista()
        ng_nuevo._NodoGeneral__listaHijos = l_nuevo
        ng_nuevo._NodoGeneral__dato = 8

        self.assertEqual(-1, self.arbol_general.nivel(ng_nuevo))

    def test_nivel_cero(self):
        self.assertEqual(0, self.arbol_general.nivel(self.ng1))

    def test_nivel(self):
        self.assertEqual(1, self.arbol_general.nivel(self.ng2))
        self.assertEqual(1, self.arbol_general.nivel(self.ng3))
        self.assertEqual(2, self.arbol_general.nivel(self.ng4))
        self.assertEqual(2, self.arbol_general.nivel(self.ng5))
        self.assertEqual(2, self.arbol_general.nivel(self.ng6))
        self.assertEqual(2, self.arbol_general.nivel(self.ng7))



if __name__ == '__main__':
    unittest.main()
