import sys
from ocho_puzzle import ocho_puzzle
sys.setrecursionlimit(500000)


if __name__ == "__main__":
    #puzzle = ocho_puzzle("123H56478")
    puzzle = ocho_puzzle("87653H241")
    #puzzle.algoritmo_anchura()
    #puzzle.algoritmo_profundidad()
    #puzzle.algoritmo_anchura_evalua_hijos()
    #puzzle.algoritmo_profundidad_evalua_hijos()
    #puzzle.algoritmo_better_first()
    puzzle.algoritmo_hill_climbing()
    #puzzle.algoritmo_beam(2,None)
    #puzzle.algoritmo_beam(1,None)
    #puzzle.algoritmo_beam(None,0.5)
    #puzzle.algoritmo_beam(None,0.35)
    #puzzle.algoritmo_beam(None,0.25)
    #puzzle.algoritmo_beam(4,None)