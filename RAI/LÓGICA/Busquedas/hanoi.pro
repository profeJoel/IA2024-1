%resuelve torres de hanoi
%regla mover_disco(cantidad, origen, destino, aux)

%caso base
mover_disco(1, ORIGEN, DESTINO, _ ) :-
    write('Se mueve disco tope desde el poste '),
    write(ORIGEN),
    write(' al disco '),
    write(DESTINO),
    nl.

%caso recurrente
mover_disco(CANT_DISCOS, ORIGEN, DESTINO, CUALQUIERA) :-
    CANT_DISCOS > 1,
    NUEVA_CANT_DISCOS is CANT_DISCOS -1,
    mover_disco(NUEVA_CANT_DISCOS, ORIGEN, CUALQUIERA, DESTINO),
    mover_disco(1,ORIGEN, DESTINO, _),
    mover_disco(NUEVA_CANT_DISCOS, CUALQUIERA, DESTINO, ORIGEN).