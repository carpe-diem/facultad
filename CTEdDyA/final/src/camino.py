# -*- coding: utf-8 -*-

from src.cola import Cola
from src.grafos import Vertice, Arista, Grafo
from src.heap import Heap


class Recorridos(object):

    def __dijkstra(self, grafo, origen, visitados, pesos, pv):
        #c = Cola()
        c = Heap()

        visitados[origen.getPosicion()] = True

        c.poner(0, origen)

        while not c.esVacia():
            proximo = c.sacar()

            for i in proximo.getListaAdyacentes():
                peso_actual = pesos[i.getVerticeDestino().getPosicion()]
                if peso_actual is None:
                    nuevo_peso =  i.getPeso()
                    peso_actual = nuevo_peso + 1
                else:
                    nuevo_peso = peso_actual + i.getPeso()

                if nuevo_peso < peso_actual:
                    pesos[i.getVerticeDestino().getPosicion()] = nuevo_peso
                    pv[i.getVerticeDestino().getPosicion()] = proximo

                if not visitados[i.getVerticeDestino().getPosicion()]:
                    c.poner(i.getPeso(), i.getVerticeDestino())
                    visitados[i.getVerticeDestino().getPosicion()] = True

        return pv

    def camino_minimo(self, grafo, origen):
        visitados = []
        pesos = []
        pv = []
        for i in grafo.getListaDeVertices():
            visitados.append(False)
            pesos.append(None)
            pv.append(None)
        pv = self.__dijkstra(grafo, origen, visitados, pesos, pv)
        self.imprimir(origen, pv)

    def imprimir(self, origen, pv):
        print "\nOrigen: {}".format(origen)

        for destino in pv:

            ultimo_destino = destino

            print "-------- Camino Min. TRT a {}".format(ultimo_destino)
            while origen != pv[destino.getPosicion()]:
                destino = pv[destino.getPosicion()]
                print destino
            print "-------- Fin del camino Min. a {}\n".format(ultimo_destino)






