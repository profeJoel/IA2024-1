from collections import deque
import sys, os , math
from time import sleep

from nodo import nodo
from arco import arco
from grafo import grafo
from estado import estado

sys.setrecursionlimit(1000000)

def ordenar_por_f(e):
    return e.get_f()

def ordenar_por_h(e):
    return e.get_h()

def ordenar_por_g(e):
    return e.get_g()

class a_estrella:
    def __init__(self, EI, EF, archivo_grafo):
        self.tablero = grafo(archivo_grafo)
        self.estado_inicial = estado(self.tablero.buscar_nodo(EI), None, "Inicial", 0)
        self.estado_final = estado(self.tablero.buscar_nodo(EF), None, "Final", None)

        self.estado_inicial.set_g(self.estado_inicial, 0)
        self.estado_inicial.set_h(self.estado_final)

        self.descubiertos = []
        self.por_explorar = deque()

        self.estado_actual = None

    def add(self, e):
        self.descubiertos.append(e)
        self.por_explorar.append(e)

    def pop(self):
        return self.por_explorar.popleft()

    def esta_descubierto(self, e):
        return e in self.descubiertos

    def es_final(self):
        return self.estado_actual == self.estado_final

    def mover(self, sucesor):
        destino = sucesor.get_destino() # entrega el nodo del grafo
        nuevo_estado = estado(destino, self.estado_actual, "De " + self.estado_actual.get_valor().get_nombre() + " hasta " + destino.get_nombre(), self.estado_actual.get_nivel() + 1)
        return nuevo_estado

    def buscar_padre(self, e):
        if e.get_padre() is not None:
            padre = e.get_padre()
            self.buscar_padre(padre)
        print(e)

    def traspasar_a_por_explorar(self, lista, N):
        for e in lista:
            self.add(e)
        for n in range(0,N):
            self.por_explorar.append(self.por_explorar.pop())

    def algoritmo_a_estrella(self, inicial, i):
        self.estado_actual = inicial
        sucesores = []

        if self.es_final():
            self.buscar_padre(inicial)
            print("\nAlgoritmo A* Llega a Solución\n")
            print("\nDescubiertos: " + str(len(self.descubiertos)))
            print("\nPor Explorar: " + str(len(self.por_explorar)))
            print("\nIteraciones: " + str(i))
            print("\nCoste Total: " + str(self.estado_actual.get_f()))
        else:
            movimientos = self.estado_actual.get_caminos()
            N = 0
            for movimiento in movimientos:
                estado_temporal = self.mover(movimiento)
                if not self.esta_descubierto(estado_temporal):
                    estado_temporal.set_g(self.estado_actual, movimiento.get_coste())
                    estado_temporal.set_h(self.estado_final)
                    sucesores.append(estado_temporal)
                    N += 1
            sucesores.sort(key=ordenar_por_f)
            self.traspasar_a_por_explorar(sucesores, N)

            return self.algoritmo_a_estrella(self.pop(), i+1)

    def algoritmo_avara(self, inicial, i):
        self.estado_actual = inicial
        sucesores = []

        if self.es_final():
            self.buscar_padre(inicial)
            print("\nAlgoritmo A* Llega a Solución\n")
            print("\nDescubiertos: " + str(len(self.descubiertos)))
            print("\nPor Explorar: " + str(len(self.por_explorar)))
            print("\nIteraciones: " + str(i))
            print("\nCoste Total: " + str(self.estado_actual.get_f()))
        else:
            movimientos = self.estado_actual.get_caminos()
            N = 0
            for movimiento in movimientos:
                estado_temporal = self.mover(movimiento)
                if not self.esta_descubierto(estado_temporal):
                    estado_temporal.set_g(self.estado_actual, movimiento.get_coste()) # no es necesario calcularlo, pero queda como registro del costo real de la solución
                    estado_temporal.set_h(self.estado_final)
                    sucesores.append(estado_temporal)
                    N += 1
            sucesores.sort(key=ordenar_por_h)
            self.traspasar_a_por_explorar(sucesores, N)

            return self.algoritmo_a_estrella(self.pop(), i+1)

    def algoritmo_uniforme(self, inicial, i):
        self.estado_actual = inicial
        sucesores = []

        if self.es_final():
            self.buscar_padre(inicial)
            print("\nAlgoritmo A* Llega a Solución\n")
            print("\nDescubiertos: " + str(len(self.descubiertos)))
            print("\nPor Explorar: " + str(len(self.por_explorar)))
            print("\nIteraciones: " + str(i))
            print("\nCoste Total: " + str(self.estado_actual.get_f()))
        else:
            movimientos = self.estado_actual.get_caminos()
            N = 0
            for movimiento in movimientos:
                estado_temporal = self.mover(movimiento)
                if not self.esta_descubierto(estado_temporal):
                    estado_temporal.set_g(self.estado_actual, movimiento.get_coste()) 
                    estado_temporal.set_h(self.estado_final)# no es necesario calcularlo, pero queda como registro de la estimación de distancia
                    sucesores.append(estado_temporal)
                    N += 1
            sucesores.sort(key=ordenar_por_g)
            self.traspasar_a_por_explorar(sucesores, N)

            return self.algoritmo_a_estrella(self.pop(), i+1)

    def init(self):
        self.add(self.estado_inicial)
        #self.algoritmo_a_estrella(self.pop(), 1)
        #self.algoritmo_avara(self.pop(), 1)
        self.algoritmo_uniforme(self.pop(), 1)
