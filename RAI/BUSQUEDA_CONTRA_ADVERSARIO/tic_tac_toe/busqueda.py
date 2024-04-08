from estado import estado
from collections import deque
import sys, os, math
sys.setrecursionlimit(100000)

class busqueda:
    def __init__(self, EI, s_max, s_min):
        self.estado_inicial = estado(EI, None, "Origen", 0)
        self.estado_solucion = None
        self.s_max = s_max
        self.s_min = s_min
        self.estados_descubiertos = 0

    def calcular_p(self, e, s):
        """e es el estado, y s es el simbolo del jugador"""
        m = e.get_estado()
        cant = 0
        for x in range(3):
            # Revisa todas las horizontales
            if m[x][0] in [s," "] and m[x][1] in [s," "] and m[x][2] in [s," "]:
                cant += 1
            # Revisa todas las verticales
            if m[0][x] in [s," "] and m[1][x] in [s," "] and m[2][x] in [s," "]:
                cant += 1
        #Revisa la primera diagonal
        if m[0][0] in [s," "] and m[1][1] in [s," "] and m[2][2] in [s," "]:
            cant += 1
        #Revisa la segunda diagonal
        if m[0][2] in [s," "] and m[1][1] in [s," "] and m[2][0] in [s," "]:
            cant += 1
        return cant

    def se_interpone(self, e1, e2, e3, propio, rival):
        return (e1 == propio and e2 == rival and e3 == rival) or (e1 == rival and e2 == propio and e3 == rival) or (e1 == rival and e2 == rival and e3 == propio)

    def incluir_recompensa(self, e, propio, rival):
        m = e.get_estado()
        r = 0

        for x in range(3):
            if self.se_interpone(m[x][0],m[x][1],m[x][2], propio, rival):
                r += 10
            if self.se_interpone(m[0][x],m[1][x],m[2][x], propio, rival):
                r += 10
        
        if self.se_interpone(m[0][0],m[1][1],m[2][2], propio, rival):
            r += 10
        if self.se_interpone(m[0][2],m[1][1],m[2][0], propio, rival):
            r += 10
        return r

    def encuentra_tres_en_linea(self, e, s):
        m = e.get_estado()
        for x in range(3):
            if m[x][0] == s and m[x][1] == s and m[x][2] == s:
                return True
            if m[0][x] == s and m[1][x] == s and m[2][x] == s:
                return True
        
        if m[0][0] == s and m[1][1] == s and m[2][2] == s:
            return True
        if m[0][2] == s and m[1][1] == s and m[2][0] == s:
            return True
        return False

    def encuentra_ganador(self, e):
        return self.encuentra_tres_en_linea(e,"X") or self.encuentra_tres_en_linea(e, "O")

    def ver_espacios_vacio(self, e):
        m = e.get_estado()
        vacios = []
        for i in range(3):
            for j in range(3):
                if m[i][j] == " ":
                    vacios.append([i,j])
        return vacios


    def juego_terminado(self, e):
        return len(self.ver_espacios_vacio(e)) == 0 or self.encuentra_ganador(e)

    def forzar_movimiento_ganador(self, e, propio):
        if self.encuentra_tres_en_linea(e, propio):
            return 100
        return 0      

    def mostrar_estado_actual(self, e):
        m = e.get_estado()
        print("\nTablero Actual: ")
        for i in range(3):
            print(" " + m[i][0] + " | " + m[i][1] + " | " + m[i][2] + " ")
            if i < 2:
                print("___________")


    def se_mueve_a(self, e, posicion, simbolo):
        nueva_matriz = [filas[:] for filas in e.get_estado()] # copia de matriz, valor por valor
        nueva_matriz[posicion[0]][posicion[1]] = simbolo

        return estado(nueva_matriz, e, " fila: " + str(posicion[0]) + ", columna: " + str(posicion[1]), e.get_nivel() + 1)

    def calcular_heuristica(self, e, t):
        """e es un estado, t es un valor booleano"""

        if t:
            #Cuando es el jugador 1
            return self.calcular_p(e, self.s_max) - self.calcular_p(e, self.s_min) + self.incluir_recompensa(e, self.s_max, self.s_min) + self.forzar_movimiento_ganador(e, self.s_max)
        else:
            #Cuando es el jugador 2
            return self.calcular_p(e, self.s_min) - self.calcular_p(e, self.s_max) + self.incluir_recompensa(e, self.s_min, self.s_max) + self.forzar_movimiento_ganador(e, self.s_min)
    
        
        """e es un estado, t es un valor booleano"""
        """
        if t:
            #Cuando es el jugador 1
            return self.calcular_p(e, self.s_max) - self.calcular_p(e, self.s_min) + self.forzar_movimiento_ganador(e, self.s_max)
        else:
            #Cuando es el jugador 2
            return self.calcular_p(e, self.s_min) - self.calcular_p(e, self.s_max) + self.forzar_movimiento_ganador(e, self.s_min)
        """

    def algoritmo_minimax(self, e, p, t):
        if p == 0 or self.juego_terminado(e):
            e.set_heuristica(self.calcular_heuristica(e, t))
            self.estados_descubiertos += 1
            return e.get_heuristica()

        if t: #turno de max (jugador principal)
            hijos = []
            maximo = -math.inf
            e_max = None
            posiciones_hijos = self.ver_espacios_vacio(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_max))
            for hijo in hijos:
                eval = self.algoritmo_minimax(hijo, p - 1, False)
                if eval >= maximo:
                    maximo = eval
                    e_max = [filas[:] for filas in hijo.get_estado()]
            self.estado_solucion = [filas[:] for filas in e_max] # movimiento con mejor valor de evaluación
            return maximo

        else: #turno de min (adversario)
            hijos = []
            minimo = math.inf
            e_min = None
            posiciones_hijos = self.ver_espacios_vacio(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_min))
            for hijo in hijos:
                eval = self.algoritmo_minimax(hijo, p - 1, True)
                if eval <= minimo:
                    minimo = eval
                    e_min = [filas[:] for filas in hijo.get_estado()]
            self.estado_solucion = [filas[:] for filas in e_min]
            return minimo

    def algoritmo_minimax_alpha_beta(self, e, p, alpha, beta, t):
        if p == 0 or self.juego_terminado(e):
            e.set_heuristica(self.calcular_heuristica(e, t))
            self.estados_descubiertos += 1
            return e.get_heuristica()

        if t: #turno de max (jugador principal)
            hijos = []
            maximo = -math.inf
            e_max = None
            posiciones_hijos = self.ver_espacios_vacio(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_max))
            for hijo in hijos:
                eval = self.algoritmo_minimax_alpha_beta(hijo, p - 1, alpha, beta, False)
                if eval >= maximo:
                    maximo = eval
                    e_max = [filas[:] for filas in hijo.get_estado()]

                #modificación alpha-beta
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            self.estado_solucion = [filas[:] for filas in e_max] # movimiento con mejor valor de evaluación
            return maximo

        else: #turno de min (adversario)
            hijos = []
            minimo = math.inf
            e_min = None
            posiciones_hijos = self.ver_espacios_vacio(e)
            for posicion in posiciones_hijos:
                hijos.append(self.se_mueve_a(e, posicion, self.s_min))
            for hijo in hijos:
                eval = self.algoritmo_minimax_alpha_beta(hijo, p - 1, alpha, beta, True)
                if eval <= minimo:
                    minimo = eval
                    e_min = [filas[:] for filas in hijo.get_estado()]
                
                #Modificación Alpha-Beta
                beta = min(beta,eval)
                if beta <= alpha:
                    break

            self.estado_solucion = [filas[:] for filas in e_min]
            return minimo

    def inicia_busqueda(self):
        #self.algoritmo_minimax(self.estado_inicial, 8, True)
        #self.algoritmo_minimax_alpha_beta(self.estado_inicial, 8, -math.inf, math.inf, True)
        # Profundidad iterativa
        
        mejor = -math.inf
        lista_solucion = []
        for profundidad in range(2,9):
            parcial = self.algoritmo_minimax_alpha_beta(self.estado_inicial, profundidad, -math.inf, math.inf, True)
            mejor = max(mejor, parcial)
            lista_solucion.append([self.estado_solucion, parcial])
            
        for solucion in lista_solucion:
            if solucion[1] == mejor:
                self.estado_solucion = solucion[0]
                
        print("Estados Descubiertos: " + str(self.estados_descubiertos))
        
        return self.estado_solucion