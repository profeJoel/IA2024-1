from busqueda import busqueda

class jugador:

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.cant_turnos = 0
        self.es_bot = tipo

    def set_simbolo(self, simbolo):
        self.simbolo = simbolo

    def toma_turno_automatico(self, matriz):
        if self.simbolo == "X":
            s_max = "X"
            s_min = "O"
        else:
            s_max = "O"
            s_min = "X"

        bot = busqueda(matriz, s_max, s_min)
        nueva_matriz = bot.inicia_busqueda() # entrega el mejor movimiento para ESE TURNO.
        return nueva_matriz
        
    def toma_turno_por_teclado(self, matriz):
        print("\n\nElige un espacio libre > Jugador: " + self.nombre)

        while True:
            while True:
                fila = int(input("Ingrese el numero de fila [0,2]: "))
                if fila >= 0 and fila <= 2:
                    break
            while True:
                columna = int(input("Ingrese el numero de columna [0,2]: "))
                if columna >= 0 and columna <= 2:
                    break
            if matriz[fila][columna] == " ":
                break

        matriz[fila][columna] = self.simbolo
        return matriz

    def toma_turno(self, matriz):
        self.cant_turnos += 1

        if self.es_bot:
            return self.toma_turno_automatico(matriz)
        return self.toma_turno_por_teclado(matriz)