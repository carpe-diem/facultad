Universidad Nacional Arturo Jauretche

Ingenieria en Informática

Complejidad Temporal, Estructura de Datos y Algorítmos

===================================================== 

Trabajo Práctico Final

Profesor: Roberto E. Soto

Alumno: Alberto Paparelli (Legajo: 1198)

20/11/2015

===================================================== 

Informe
=======

El código de la aplicación puede descargarse desde:
    https://github.com/carpe-diem/facultad/tree/master/CTEdDyA/final



Detalles de implementación
--------------------------

Para la realización del trabajo práctico, reutilice las clases y métodos realizados de los ejercicios de las prácticas (Listas, Colas, Grafos, etc).

Para el camino minimo y los arboles, lo primero que hace la aplicación el levantar los archivos con los datos iniciales, y luego genera los grafos y arboles.



Caminos con mínimo TRT
~~~~~~~~~~~~~~~~~~~~~~

Con el grafo armado, armo un algoritmo tipo BFS.

Utilizo, 3 vectores (peso, visitados, y otro para el vecino previo).
Lugo aplicando dijkstra obtengo los caminos minimos. En lugar de colas, utilizo Colas de Heap, para poder mejorar la performance, ya que de esta manera, 
puedo ponerle prioridades a la cola.


Arboles TRT
~~~~~~~~~~~

En este algorítmo, se utilizan arboles Generales.

El Arbol se arma a partir de una ciudad, y se completa por niveles.



Problemas Encotrados
--------------------

1) Uno de los principales problemas fue subestimar tanto la complejidad como los tiempo. Por este motivo, no pude realizar UnitTest.

2) En Caminos con mínimo TRT para poder utilizar dijkstra bien y elegir primero el vecino con mayor prioridad, La manera de solucionarlo fue utilizar una libreria de python llamada heapq (recomendación del profesor).

3) En Arboles, el principal problema fue ajustar los métodos de las clases que tenía, y terminar algunos (Incluye y nivel), ya que nivel lo utilizo para generar la impresión.



Condiciones de ejecución
-------------------------

El programa corre en cualquier computadora que tenga instalado python 2.7.

Ejecución: python main.py


Mejoras a hacerle
-----------------

* Pasarle los archivos con los datos iniciales por parametro.
* Elección de arbol o camino minímo por parametro.
* Desharcodear impresion, para poder utilizar como libreria externa.
* Posibilidad de generar imagenes graficas a partir de los resultados).

