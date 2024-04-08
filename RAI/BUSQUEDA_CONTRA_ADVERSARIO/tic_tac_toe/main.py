from jugador import jugador
from tablero import tablero

#MAIN
if __name__ == "__main__":
    print("*********BIENVENIDOS AL GATO*********")
    nombre = input("Ingrese el nombre del Usuario 1: ")
    humano = jugador(nombre, False)
    
    #nombre = input("Ingrese el nombre del Usuario 2: ")
    #humano2 = jugador(nombre)

    bot = jugador("BOT", True)

    #tictactoe = tablero(humano, humano2)
    tictactoe = tablero(humano, bot)
    #tictactoe = tablero(bot, humano)
    
    tictactoe.inicia_partida()
