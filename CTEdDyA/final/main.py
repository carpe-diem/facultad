# -*- coding: utf-8 -*-

from src.arboles import ArbolesTRT
from src.camino import Grafo, Vertice, Recorridos
from src.utils import Ciudades


debug = False


def main():
    ciudades = Ciudades().ciudades()

    if debug:
        for k, v in ciudades.items():
            print u"Indice: {k} - {v}".format(
                k=k, v=v)

    grafo = Grafo()

    for key, value in ciudades.items():
        vertice = Vertice(value.get('nombre'), key)
        grafo.agregarVertice(vertice)

        #TODO Borrar
        if key == 0:
            v1=vertice

    trt = [
                [0,0,0,0,0,0,0,0,0,6,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,2,0,0,0,0],
                [0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
                [0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,2,0,5,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,6,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0],
                [0,0,0,4,0,0,0,0,0,0,0,0,0,1,0,3,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,3,0,0,0,0,2,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0],
                [6,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,3,0,0,0,0,0,0],
                [0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,5,0,0,7,0,4,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,7,0,3,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,1,0,0,0,0,0,3,0,0,2,0,0,6,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,3,0,5,0,0,0,0,2,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,2,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,2,0,0,0,0,0,0,0,0,0,0,4,6,0,0,0,0,0,0,0,0,0],
                [0,0,0,5,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,5,0]
            ]

    for x in range(len(trt)):
        for y in range(len(trt[x])):
            peso = trt[x][y]
            if peso:
                if debug == True:
                    print "Conecto {a} con {b} ->> peso: {c}".format(
                        a=grafo.vertice(x), b=grafo.vertice(y), c=peso)
                grafo.conectar(grafo.vertice(x), grafo.vertice(y), peso)

    recorrido = Recorridos()
    recorrido.camino_minimo(grafo, v1)

    ArbolesTRT(ciudades, trt).generar_arboles()


if __name__ == "__main__":
   main()

