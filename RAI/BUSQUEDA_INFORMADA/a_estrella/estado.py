from nodo import nodo
from arco import arco
from grafo import grafo

import math

class estado:

    def __init__(self, nodo, padre, accion, nivel):
        self.valor = nodo
        self.padre = padre
        self.accion = accion
        self.nivel = nivel
        self.g = -1
        self.h = -1
        self.f = -1

    def get_valor(self):
        return self.valor

    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion
    
    def get_nivel(self):
        return self.nivel

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def get_f(self):
        return self.g+self.h

    def get_caminos(self):
        return self.valor.get_caminos()

    def set_g(self, e, coste):
        if e is None:
            self.g = -1
        else:
            g_acumulado = e.get_g() if e.get_g()>0 else 0
            self.g = g_acumulado + coste

    def set_h(self, e):
        if e is None:
            self.h = -1
        elif type(e) == int and e == 0:
            self.h == 0

        else:
            objetivo = e.get_valor()
            #calcular distancia euclidiana
            self.h = math.sqrt((objetivo.get_y()-self.valor.get_y())**2+(objetivo.get_x()-self.valor.get_x())**2)

    def __eq__(self, o: object) -> bool:
        if o is None:
            return False
        return self.valor == o.get_valor()

    def __str__(self):
        return "Estado " + str(self.valor) + "\nAccion: " + self.accion + "\nNivel: " + str(self.nivel) + "\nG(e): " + str(self.g) + "\nH(e): " + str(self.h) + "\nF(e): " + str(self.g+self.h) + "\n"