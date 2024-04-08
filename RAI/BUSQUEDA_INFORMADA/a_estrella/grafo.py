from nodo import nodo
from arco import arco

class grafo:
    def __init__(self, archivo_grafo) -> None:
        self.nodos = []
        self.arcos = []
        self.lee_archivo_grafo(archivo_grafo)
    
    def get_nodo(self, indice):
        return self.nodos[indice]

    def get_arco(self, indice):
        return self.arcos[indice]

    def add_nodo(self, x, y, nombre):
        nuevo = nodo(x, y, nombre)
        self.nodos.append(nuevo)

    def add_arco(self, origen, destino, coste):
        nuevo = arco(origen, destino, coste)
        origen.add_camino(nuevo)
        self.arcos.append(nuevo)

    def lee_archivo_grafo(self, archivo):
        with open(archivo) as en_archivo:
            for linea in en_archivo:
                posicion = linea.split(' ')
                x = float(posicion[0])
                y = float(posicion[1])

                aux = nodo(x,y, posicion[2])
                if aux not in self.nodos:
                    self.add_nodo(x,y,posicion[2])
                origen = self.nodos[self.nodos.index(aux)]

                x = float(posicion[3])
                y = float(posicion[4])

                aux = nodo(x,y, posicion[5])
                if aux not in self.nodos:
                    self.add_nodo(x,y,posicion[5])
                destino = self.nodos[self.nodos.index(aux)]

                coste = float(posicion[6])

                self.add_arco(origen, destino, coste)

    def buscar_nodo(self, n):
        if n not in self.nodos:
            self.add_nodo(n.get_x(), n.get_y(), n.get_nombre())
        return self.nodos[self.nodos.index(n)]

    def __str__(self) -> str:
        salida = "\nNODOS:\n"
        for n in self.nodos:
            salida += str(n) + " = ["
            for c in n.get_caminos():
                salida += str(c) + ", "
            salida += "]\n"
        
        salida = "\nARCOS:\n"
        for a in self.arcos:
            salida += str(a) + "\n"

        return "El grafo es: " + salida
