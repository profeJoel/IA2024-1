from nodo import nodo

class arco:

    def __init__(self, origen, destino, coste) -> None:
        self.origen = origen
        self.destino = destino
        self.coste = coste

    def get_origen(self):
        return self.origen

    def get_destino(self):
        return self.destino

    def get_coste(self):
        return self.coste

    def __eq__(self, o: object) -> bool:
        if o == None:
            return False
        return self.origen == o.get_origen() and self.destino == o.get_destino() and self.coste == o.get_coste()

    def __str__(self) -> str:
        """|origen|-coste->|destino|"""

        return "|" + str(self.origen) + "| -" + str(self.coste) + "-> |" + str(self.destino) + "|"
