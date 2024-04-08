class nodo:

    def __init__(self, x, y, nombre):
        self.x = x
        self.y = y
        self.nombre = nombre
        self.caminos = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_nombre(self):
        return self.nombre

    def get_cammino(self, indice):
        return self.caminos[indice]

    def get_caminos(self):
        return self.caminos
    
    def add_camino(self, nuevo):
        return self.caminos.append(nuevo)

    def __eq__(self, o: object) -> bool:
        if o == None:
            return False
        return self.x == o.get_x() and self.y == o.get_y()

    def __str__(self) -> str:
        """[NOMBRE (X,Y)]"""
        return "[" + self.nombre + " (" + str(self.x) + "," + str(self.y) + ")]"

    

    