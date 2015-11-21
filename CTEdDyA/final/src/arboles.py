# -*- coding: utf-8 -*-

from src.arbol_general import NodoGeneral, ArbolGeneral
from src.cola import Cola
from src.listaenlazada import Recorredor


class ArbolesTRT(object):
    total = 0

    def __init__(self, ciudades, trts):
        self.ciudades = ciudades
        self.trts = trts
        self.total = len(ciudades)

    def __arbol(self, arbol, ciudad_id, lista):

        tiempos = self.trts[ciudad_id]

        pos_aux = []
        for pos in range(self.total):

            if tiempos[pos] and not lista[pos]:
                nodo = NodoGeneral()
                nodo.setDato(self.ciudades[pos].get('nombre'), tiempos[pos])
                #new_arbol = ArbolGeneral(nodo)
                #arbol.agregarHijo(new_arbol)
                arbol.agregarHijo(nodo)
                #print "agrego Arbol {} a {}".format(new_arbol, arbol)
                lista[pos] = True
                pos_aux.append(pos)
                #self.__arbol(new_arbol, pos, lista)

        rec_hijos = arbol.getHijos().recorredor()
        try:
            rec_hijos.comenzar()
            pos = 0
            while not rec_hijos.fin():
                self.__arbol(rec_hijos.elemento(), pos_aux[pos], lista)
                rec_hijos.proximo()
                pos += 1
        except:
            pass

    def crear_lista(self):
        lista = []
        for x in range(self.total):
            lista.append(False)

        return lista

    def generar_arboles(self):
        for ciudad in self.ciudades.items():
            lista = self.crear_lista()
            nodo_raiz = NodoGeneral()
            nodo_raiz.setDato(self.ciudades[ciudad[0]].get('nombre'), 0)
            arbol = ArbolGeneral(nodo_raiz)
            #lista[0] = True
            lista[ciudad[0]] = True
            self.__arbol(arbol, ciudad[0], lista)

            self.imprimir(arbol)

    def imprimir(self, arbol):
        niveles = {}

        for x in range(arbol.altura() + 1):
            niveles[x] = []

        cola = Cola()
        cola.poner(arbol)

        while not cola.esVacia():
            new_arbol = cola.sacar()
            nivel = arbol.nivel(new_arbol)

            niveles[nivel].append(new_arbol.getDatoRaiz())

            if not new_arbol.getHijos().esVacia():
                rec_hijos = new_arbol.getHijos().recorredor()
                rec_hijos.comenzar()
                while not rec_hijos.fin():

                    cola.poner(rec_hijos.elemento())
                    rec_hijos.proximo()

        print "-------- Comienzo de Árbol TRT --------"
        for nivel, datos in niveles.items():
            if nivel == 0:
                texto = "Raiz: {}"
            else:
                texto = "nivel {}: ".format(nivel) + "{}"

            print texto.format(', '.join(map(str, datos)))
        print "-------- Fin de Árbol TRT --------\n"


