# -*- coding: utf-8 -*-
import unittest

from listaenlazada import Lista, ListaEnlazada, Nodo, Recorredor, \
    ListaConPyLista


class TestLista(unittest.TestCase):

    def test_verificar_abstract_class(self):
        self.assertRaises(Exception, Lista)
        self.assertTrue(Lista.__dict__.has_key('__metaclass__'))

    def test_verificar_abstract_methods(self):
        self.assertTrue(Lista.__dict__['elemento'].__isabstractmethod__)
        self.assertTrue(Lista.__dict__['agregar'].__isabstractmethod__)
        self.assertTrue(Lista.__dict__['eliminar'].__isabstractmethod__)
        self.assertTrue(Lista.__dict__['esVacia'].__isabstractmethod__)
        self.assertTrue(Lista.__dict__['incluye'].__isabstractmethod__)

    def test_get_tamanio_inicial(self):
        self.assertEqual(0, ListaEnlazada().getTamanio())

    def test_get_tamanio(self):
        lista = ListaEnlazada()
        self.assertEqual(0, lista.getTamanio())
        lista._tamanio += 1
        self.assertEqual(1, lista.getTamanio())
        lista._tamanio += 1
        self.assertEqual(2, lista.getTamanio())

    def test_recorredor(self):
        lista = ListaEnlazada()
        recorredor = Recorredor
        recorredor2 = Recorredor(lista)
        self.assertIsInstance(lista.recorredor(), recorredor)
        self.assertEqual(lista.recorredor()._lista, recorredor2._lista)


class TestNodo(unittest.TestCase):

    def test_atributo_dato_none(self):
        nodo = Nodo()
        self.assertEqual(None, nodo._dato)

    def test_atributo_siguiente_none(self):
        nodo = Nodo()
        self.assertEqual(None, nodo._siguiente)

    def test_get_dato(self):
        nodo = Nodo()
        self.assertEqual(None, nodo.getDato())
        nodo._dato = 1
        self.assertEqual(1, nodo.getDato())

    def test_set_dato(self):
        nodo = Nodo()
        nodo.setDato('dummy')
        self.assertEqual('dummy', nodo.getDato())

    def test_get_siguiente(self):
        nodo = Nodo()
        self.assertEqual(None, nodo.getSiguiente())
        nodo._siguiente = 1
        self.assertEqual(1, nodo.getSiguiente())

    def test_set_siguiente(self):
        nodo = Nodo()
        nodo.setSiguiente('dummy')
        self.assertEqual('dummy', nodo.getSiguiente())

    def test_str(self):
        DUMMY = 'dummy_str'
        DUMMY_STR = 'Nodo <dummy_str>'
        nodo = Nodo()
        nodo.setDato(DUMMY)
        self.assertEqual(DUMMY_STR, str(nodo))


class TestListaEnlazada(unittest.TestCase):

    def test_lista_inicio_none(self):
        lista = ListaEnlazada()
        self.assertEqual(None, lista._inicio)

    def test_lista_vacia_si(self):
        lista = ListaEnlazada()
        self.assertTrue(lista.esVacia())

    def test_lista_vacia_no(self):
        lista = ListaEnlazada()
        lista.agregar('dummy', 0)
        self.assertFalse(lista.esVacia())

    def test_str(self):
        lista = ListaEnlazada()
        lista.agregar(1, 0)
        lista.agregar(2, 1)
        lista.agregar(3, 2)
        self.assertEqual('[1, 2, 3]', str(lista))

    def test_elemento_lista_vacia(self):
        lista = ListaEnlazada()
        self.assertRaises(IndexError, lista.elemento, 0)

    def test_elemento_pos_menor_cero(self):
        lista = ListaEnlazada()
        self.assertRaises(IndexError, lista.elemento, -1)

    def test_elemento_posicion(self):
        lista = ListaEnlazada()
        self.assertRaises(IndexError, lista.elemento, 0)

    def test_elemento_en_posiciones_ordenadas(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        self.assertEqual('dummy_0', lista.elemento(0))
        lista.agregar('dummy_1', 1)
        self.assertEqual('dummy_1', lista.elemento(1))
        lista.agregar('dummy_2', 2)
        self.assertEqual('dummy_2', lista.elemento(2))
        lista.agregar('dummy_3', 3)
        self.assertEqual('dummy_3', lista.elemento(3))

    def test_elemento_en_posiciones_desordenadas(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        self.assertEqual('dummy_0', lista.elemento(0))
        lista.agregar('dummy_1', 1)
        self.assertEqual('dummy_0', lista.elemento(0))
        self.assertEqual('dummy_1', lista.elemento(1))
        lista.agregar('dummy_2', 2)
        self.assertEqual('dummy_0', lista.elemento(0))
        self.assertEqual('dummy_1', lista.elemento(1))
        self.assertEqual('dummy_2', lista.elemento(2))
        lista.agregar('dummy_4', 1)
        self.assertEqual('dummy_0', lista.elemento(0))
        self.assertEqual('dummy_4', lista.elemento(1))
        self.assertEqual('dummy_1', lista.elemento(2))
        self.assertEqual('dummy_2', lista.elemento(3))
        lista.agregar('dummy_5', 2)
        self.assertEqual('dummy_0', lista.elemento(0))
        self.assertEqual('dummy_4', lista.elemento(1))
        self.assertEqual('dummy_5', lista.elemento(2))
        self.assertEqual('dummy_1', lista.elemento(3))
        self.assertEqual('dummy_2', lista.elemento(4))

        lista.agregar('dummy_6', 0)
        self.assertEqual('dummy_6', lista.elemento(0))
        self.assertEqual('dummy_0', lista.elemento(1))
        self.assertEqual('dummy_4', lista.elemento(2))
        self.assertEqual('dummy_5', lista.elemento(3))
        self.assertEqual('dummy_1', lista.elemento(4))
        self.assertEqual('dummy_2', lista.elemento(5))

    def test_agregar_a_lista_pos_menor_0(self):
        lista = ListaEnlazada()
        self.assertRaises(IndexError, lista.agregar,'dummy', -1)

    def test_agregar_a_lista_pos_mayor_tamanio_lista(self):
        lista = ListaEnlazada()
        self.assertRaises(IndexError, lista.agregar,'dummy', 1)
        lista._tamanio = 1
        self.assertRaises(IndexError, lista.agregar,'dummy', 2)

    def test_agregar_a_lista_nueva(self):
        lista = ListaEnlazada()
        lista.agregar('dummy1', 0)
        self.assertEqual(1, lista._tamanio)
        lista.agregar('dummy2', 1)
        self.assertEqual(2, lista._tamanio)
        lista.agregar('dummy3', 2)
        self.assertEqual(3, lista._tamanio)
        lista.agregar('dummy4', 1)
        self.assertEqual(4, lista._tamanio)

    def test_agregar_a_lista_existente_en_orden(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        self.assertEqual(2, lista._tamanio)
        lista.agregar('dummy_2', 2)
        self.assertEqual(3, lista._tamanio)

    def test_agregar_a_lista_existente_sin_orden(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        self.assertEqual(2, lista._tamanio)
        lista.agregar('dummy_2', 2)
        self.assertEqual(3, lista._tamanio)

        lista.agregar('dummy_4', 1)
        self.assertEqual(4, lista._tamanio)

    def test_incluye_lista_vacia(self):
        lista = ListaEnlazada()
        self.assertFalse(lista.incluye('dummy_0'))

    def test_incluye_existe(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        lista.agregar('dummy_2', 2)
        lista.agregar('dummy_3', 3)

        self.assertTrue(lista.incluye('dummy_0'))
        self.assertTrue(lista.incluye('dummy_1'))
        self.assertTrue(lista.incluye('dummy_2'))
        self.assertTrue(lista.incluye('dummy_3'))

    def test_incluye_no_existe(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        lista.agregar('dummy_2', 2)
        lista.agregar('dummy_3', 3)
        self.assertFalse(lista.incluye('dummy_4'))
        self.assertFalse(lista.incluye('dummy_5'))

    def test_eliminar_index_error(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        lista.agregar('dummy_2', 2)
        lista.agregar('dummy_3', 3)

    def test_eliminar_ok(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.eliminar(0)
        self.assertTrue(lista.esVacia())
        self.assertFalse(lista.incluye('dummy0'))

        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        lista.agregar('dummy_2', 2)
        lista.agregar('dummy_3', 3)
        tamanio = lista.getTamanio()

        lista.eliminar(2)
        self.assertEqual(tamanio - 1, lista.getTamanio())
        self.assertFalse(lista.incluye('dummy2'))

        lista.eliminar(2)
        self.assertEqual(tamanio - 2, lista.getTamanio())
        self.assertFalse(lista.incluye('dummy3'))

        lista.eliminar(0)
        self.assertEqual(tamanio - 3, lista.getTamanio())
        self.assertFalse(lista.incluye('dummy0'))

        lista.eliminar(0)
        self.assertEqual(tamanio - 4, lista.getTamanio())
        self.assertFalse(lista.incluye('dummy1'))

    def test_eliminar_pos_error(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        lista.agregar('dummy_2', 2)
        tamanio = lista.getTamanio()

        self.assertRaises(IndexError, lista.eliminar, 3)
        self.assertRaises(IndexError, lista.eliminar, 4)
        self.assertRaises(IndexError, lista.eliminar, -1)

        self.assertEqual(tamanio, lista.getTamanio())
        self.assertTrue(lista.incluye('dummy_0'))
        self.assertTrue(lista.incluye('dummy_1'))
        self.assertTrue(lista.incluye('dummy_2'))

class TestRecorredor(unittest.TestCase):

    def setUp(self):
        self.lista_vacia = ListaEnlazada()

        self.ELEM_0 = 'dummy_0'
        self.ELEM_1 = 'dummy_1'
        self.ELEM_2 = 'dummy_2'

        self.lista1 = ListaEnlazada()
        self.lista1.agregar(self.ELEM_0, 0)

        self.lista2 = ListaEnlazada()
        self.lista2.agregar(self.ELEM_0, 0)
        self.lista2.agregar(self.ELEM_1, 1)

        self.lista3 = ListaEnlazada()
        self.lista3.agregar(self.ELEM_0, 0)
        self.lista3.agregar(self.ELEM_1, 1)
        self.lista3.agregar(self.ELEM_2, 2)

        self.lista_vacia_py = ListaConPyLista()

        self.lista_py_1 = ListaConPyLista()
        self.lista_py_1.agregar(self.ELEM_0, 0)

        self.lista_py_2 = ListaConPyLista()
        self.lista_py_2.agregar(self.ELEM_0, 0)
        self.lista_py_2.agregar(self.ELEM_1, 1)

        self.lista_py_3 = ListaConPyLista()
        self.lista_py_3.agregar(self.ELEM_0, 0)
        self.lista_py_3.agregar(self.ELEM_1, 1)
        self.lista_py_3.agregar(self.ELEM_2, 2)

    def test_inicio(self):
        rec = Recorredor(self.lista_vacia)
        self.assertEqual(self.lista_vacia, rec._lista)
        self.assertEqual(None, rec._actual)

        rec2 = Recorredor(self.lista3)
        self.assertEqual(self.lista3, rec2._lista)
        self.assertEqual(None, rec2._actual)


        recpy = Recorredor(self.lista_vacia_py)
        self.assertEqual(self.lista_vacia_py, recpy._lista)
        self.assertEqual(None, recpy._actual)

        rec2 = Recorredor(self.lista3)
        self.assertEqual(self.lista3, rec2._lista)
        self.assertEqual(None, rec2._actual)

    def test_comenzar_vacia(self):
        rec = Recorredor(self.lista_vacia)
        self.assertRaises(StopIteration, rec.comenzar)

        recpy = Recorredor(self.lista_vacia_py)
        self.assertRaises(StopIteration, rec.comenzar)

    def test_comenzar_no_vacia(self):
        rec1 = Recorredor(self.lista1)
        rec2 = Recorredor(self.lista2)
        rec3 = Recorredor(self.lista3)

        rec1.comenzar()
        rec2.comenzar()
        rec3.comenzar()

        self.assertEqual(0, rec1._actual)
        self.assertEqual(0, rec2._actual)
        self.assertEqual(0, rec3._actual)

        recpy1 = Recorredor(self.lista_py_1)
        recpy2 = Recorredor(self.lista_py_2)
        recpy3 = Recorredor(self.lista_py_3)

        recpy1.comenzar()
        recpy2.comenzar()
        recpy3.comenzar()

        self.assertEqual(0, recpy1._actual)
        self.assertEqual(0, recpy2._actual)
        self.assertEqual(0, recpy3._actual)

    def test_elemento(self):
        rec = Recorredor(self.lista3)
        rec.comenzar()

        rec._actual = 0
        self.assertEqual(self.ELEM_0, rec.elemento())

        rec._actual = 1
        self.assertEqual(self.ELEM_1, rec.elemento())

        rec._actual = 2
        self.assertEqual(self.ELEM_2, rec.elemento())

        recpy = Recorredor(self.lista_py_3)
        recpy.comenzar()

        recpy._actual = 0
        self.assertEqual(self.ELEM_0, recpy.elemento())

        recpy._actual = 1
        self.assertEqual(self.ELEM_1, recpy.elemento())

        recpy._actual = 2
        self.assertEqual(self.ELEM_2, recpy.elemento())

    def test_proximo_no_hay(self):
        rec = Recorredor(self.lista1)
        rec.comenzar()
        self.assertRaises(StopIteration, rec.proximo)

        rec2 = Recorredor(self.lista3)
        rec2._actual = 2
        self.assertRaises(StopIteration, rec2.proximo)

        recpy = Recorredor(self.lista_py_1)
        recpy.comenzar()
        self.assertRaises(StopIteration, recpy.proximo)

        recpy2 = Recorredor(self.lista_py_3)
        recpy2._actual = 2
        self.assertRaises(StopIteration, recpy2.proximo)

    def test_proximo(self):
        rec = Recorredor(self.lista3)
        rec.comenzar()
        rec.proximo()

        self.assertEqual(self.ELEM_1, rec.elemento())
        rec.proximo()

        self.assertEqual(self.ELEM_2, rec.elemento())

        self.assertRaises(StopIteration, rec.proximo)

        recpy = Recorredor(self.lista_py_3)
        recpy.comenzar()
        recpy.proximo()

        self.assertEqual(self.ELEM_1, recpy.elemento())
        recpy.proximo()

        self.assertEqual(self.ELEM_2, recpy.elemento())

        self.assertRaises(StopIteration, recpy.proximo)

    def test_fin_si(self):
        rec1 = Recorredor(self.lista1)
        rec2 = Recorredor(self.lista2)
        rec3 = Recorredor(self.lista3)

        rec1._actual = 0
        rec2._actual = 1
        rec3._actual = 2

        self.assertTrue(rec1.fin())
        self.assertTrue(rec2.fin())
        self.assertTrue(rec3.fin())

        recpy1 = Recorredor(self.lista_py_1)
        recpy2 = Recorredor(self.lista_py_2)
        recpy3 = Recorredor(self.lista_py_3)

        recpy1._actual = 0
        recpy2._actual = 1
        recpy3._actual = 2

        self.assertTrue(recpy1.fin())
        self.assertTrue(recpy2.fin())
        self.assertTrue(recpy3.fin())
        recpy1 = Recorredor(self.lista_py_1)
        recpy2 = Recorredor(self.lista_py_2)
        recpy3 = Recorredor(self.lista_py_3)

        recpy1._actual = 0
        recpy2._actual = 1
        recpy3._actual = 2

        self.assertTrue(recpy1.fin())
        self.assertTrue(recpy2.fin())
        self.assertTrue(recpy3.fin())

    def test_fin_no(self):
        rec2 = Recorredor(self.lista2)
        rec3 = Recorredor(self.lista3)

        rec2._actual = 0
        rec3._actual = 0

        self.assertFalse(rec2.fin())
        self.assertFalse(rec3.fin())

        rec3._actual = 1
        self.assertFalse(rec3.fin())

        recpy2 = Recorredor(self.lista_py_2)
        recpy3 = Recorredor(self.lista_py_3)

        recpy2._actual = 0
        recpy3._actual = 0

        self.assertFalse(recpy2.fin())
        self.assertFalse(recpy3.fin())

        recpy3._actual = 1
        self.assertFalse(recpy3.fin())

    def test_agregar(self):
        NEW_DUMMY_0 = 'new_dummy_0'
        NEW_DUMMY_1 = 'new_dummy_1'
        NEW_DUMMY_2 = 'new_dummy_2'

        rec = Recorredor(self.lista3)

        rec._actual = 0
        rec.agregar(NEW_DUMMY_0)
        self.assertEqual(NEW_DUMMY_0, rec.elemento())
        self.assertEqual(NEW_DUMMY_0, self.lista3.elemento(0))

        rec._actual = 1
        rec.agregar(NEW_DUMMY_1)
        self.assertEqual(NEW_DUMMY_1, rec.elemento())
        self.assertEqual(NEW_DUMMY_1, self.lista3.elemento(1))

        rec._actual = 2
        rec.agregar(NEW_DUMMY_2)
        self.assertEqual(NEW_DUMMY_2, rec.elemento())
        self.assertEqual(NEW_DUMMY_2, self.lista3.elemento(2))

        recpy = Recorredor(self.lista_py_3)

        recpy._actual = 0
        recpy.agregar(NEW_DUMMY_0)
        self.assertEqual(NEW_DUMMY_0, recpy.elemento())
        self.assertEqual(NEW_DUMMY_0, self.lista_py_3.elemento(0))

        recpy._actual = 1
        recpy.agregar(NEW_DUMMY_1)
        self.assertEqual(NEW_DUMMY_1, recpy.elemento())
        self.assertEqual(NEW_DUMMY_1, self.lista_py_3.elemento(1))

        recpy._actual = 2
        recpy.agregar(NEW_DUMMY_2)
        self.assertEqual(NEW_DUMMY_2, recpy.elemento())
        self.assertEqual(NEW_DUMMY_2, self.lista_py_3.elemento(2))

    def test_eliminar(self):
        rec = Recorredor(self.lista3)
        tamanio = self.lista3.getTamanio()
        rec._actual = 2

        rec.eliminar()
        self.assertEqual(tamanio - 1, self.lista3.getTamanio())

        rec.eliminar()
        self.assertEqual(tamanio - 2, self.lista3.getTamanio())

        rec.eliminar()
        self.assertEqual(tamanio - 3, self.lista3.getTamanio())

        recpy = Recorredor(self.lista_py_3)
        tamanio = self.lista_py_3.getTamanio()
        recpy._actual = 2

        recpy.eliminar()
        self.assertEqual(tamanio - 1, self.lista_py_3.getTamanio())

        recpy.eliminar()
        self.assertEqual(tamanio - 2, self.lista_py_3.getTamanio())

        recpy.eliminar()
        self.assertEqual(tamanio - 3, self.lista_py_3.getTamanio())


class TestListaConPyListas(unittest.TestCase):

    def setUp(self):
        self.lista = ListaConPyLista()

    def test_lista_inicio_none(self):
        self.assertEqual([], self.lista._datos)

    def test_lista_vacia_si(self):
        self.assertTrue(self.lista.esVacia())

    def test_lista_vacia_no(self):
        self.lista._datos = [1, 2, 3, 4]
        self.lista._tamanio = 4
        self.assertFalse(self.lista.esVacia())

    def test_str(self):
        self.assertEqual("[]", str(self.lista))
        self.lista._datos = [1, 2, 3, 4]
        self.lista._tamanio = 4
        self.assertEqual("[1, 2, 3, 4]", str(self.lista))

    def test_elemento_lista_vacia(self):
        self.assertRaises(IndexError, self.lista.elemento, 0)
        self.assertRaises(IndexError, self.lista.elemento, 2)

    def test_elemento_pos_menor_cero(self):
        self.assertRaises(IndexError, self.lista.elemento, -1)

    def test_elemento_en_posiciones_ordenadas(self):
        self.lista._datos = ['dummy_0','dummy_1','dummy_2','dummy_3']
        self.lista._tamanio = 4

        self.assertEqual('dummy_0', self.lista.elemento(0))
        self.assertEqual('dummy_1', self.lista.elemento(1))
        self.assertEqual('dummy_2', self.lista.elemento(2))
        self.assertEqual('dummy_3', self.lista.elemento(3))

    def test_elemento_en_posiciones_desordenadas(self):
        self.lista._datos = ['dummy_0','dummy_1','dummy_2','dummy_3']
        self.lista._tamanio = 4

        self.assertEqual('dummy_3', self.lista.elemento(3))
        self.assertEqual('dummy_1', self.lista.elemento(1))
        self.assertEqual('dummy_0', self.lista.elemento(0))
        self.assertEqual('dummy_2', self.lista.elemento(2))

    def test_agregar_a_lista_pos_menor_0(self):
        self.assertRaises(IndexError, self.lista.agregar,'dummy', -1)

    def test_agregar_a_lista_pos_mayor_tamanio_lista(self):
        self.assertRaises(IndexError, self.lista.agregar,'dummy', 1)
        self.lista._tamanio = 1
        self.assertRaises(IndexError, self.lista.agregar,'dummy', 2)

    def test_agregar_a_lista_nueva(self):
        self.lista.agregar('dummy_0', 0)
        self.assertEqual('dummy_0', self.lista.elemento(0))

        self.lista.agregar('dummy_1', 1)
        self.assertEqual('dummy_1', self.lista.elemento(1))

        self.lista.agregar('dummy_2', 0)
        self.assertEqual('dummy_2', self.lista.elemento(0))
        self.assertEqual('dummy_0', self.lista.elemento(1))
        self.assertEqual('dummy_1', self.lista.elemento(2))


    def test_incluye_lista_vacia(self):
        self.assertFalse(self.lista.incluye('dummy_0'))

    def test_incluye_existe(self):
        self.lista._datos = ['dummy_0','dummy_1','dummy_2','dummy_3']
        self.lista._tamanio = 4

        self.assertTrue(self.lista.incluye('dummy_0'))
        self.assertTrue(self.lista.incluye('dummy_1'))
        self.assertTrue(self.lista.incluye('dummy_2'))
        self.assertTrue(self.lista.incluye('dummy_3'))

    def test_incluye_no_existe(self):
        self.lista._datos = ['dummy_0','dummy_1','dummy_2','dummy_3']
        self.assertFalse(self.lista.incluye('dummy_4'))
        self.assertFalse(self.lista.incluye('dummy_5'))

    def test_eliminar_index_error(self):
        lista = ListaEnlazada()
        lista.agregar('dummy_0', 0)
        lista.agregar('dummy_1', 1)
        lista.agregar('dummy_2', 2)
        lista.agregar('dummy_3', 3)

    def test_eliminar_ok(self):
        self.lista._datos = ['dummy_0']
        self.lista._tamanio = 1
        self.lista.eliminar(0)
        self.assertTrue(self.lista.esVacia())
        self.assertFalse(self.lista.incluye('dummy0'))

        self.lista._datos = ['dummy_0','dummy_1','dummy_2','dummy_3']
        self.lista._tamanio = 4
        tamanio = self.lista.getTamanio()

        self.lista.eliminar(2)
        self.assertEqual(tamanio - 1, self.lista.getTamanio())
        self.assertFalse(self.lista.incluye('dummy2'))

        self.lista.eliminar(2)
        self.assertEqual(tamanio - 2, self.lista.getTamanio())
        self.assertFalse(self.lista.incluye('dummy3'))

        self.lista.eliminar(0)
        self.assertEqual(tamanio - 3, self.lista.getTamanio())
        self.assertFalse(self.lista.incluye('dummy0'))

        self.lista.eliminar(0)
        self.assertEqual(tamanio - 4, self.lista.getTamanio())
        self.assertFalse(self.lista.incluye('dummy1'))

    def test_eliminar_pos_error(self):
        self.lista._datos = ['dummy_0','dummy_1','dummy_2']
        self.lista._tamanio = 34

        tamanio = self.lista.getTamanio()

        self.assertRaises(IndexError, self.lista.eliminar, 3)
        self.assertRaises(IndexError, self.lista.eliminar, 4)
        self.assertRaises(IndexError, self.lista.eliminar, -1)

        self.assertEqual(tamanio, self.lista.getTamanio())
        self.assertTrue(self.lista.incluye('dummy_0'))
        self.assertTrue(self.lista.incluye('dummy_1'))
        self.assertTrue(self.lista.incluye('dummy_2'))


if __name__ == '__main__':
    unittest.main()
