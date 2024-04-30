# Hechos
humano(hitler).
humano(osama_bin_laden).

perro(cholito).
perro(zeus).

# Relaciones.
amo(hitler,zeus).
amo(osama_bin_laden,cholito).

mascota(P,H):- amo(H,P).

#amo(H,P):-humano(H),perro(P).
