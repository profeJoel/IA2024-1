ciudad(chillan).
ciudad(putaendo).
ciudad(calbuco).
ciudad(melipilla).
ciudad(chonchi).

temp_f(chillan, 70).
temp_f(putaendo, 80).
temp_f(calbuco, 50).
temp_f(melipilla, 70).
temp_f(chonchi, 40).

%realizar la transformacion de farenheit a celcius
temp_c(CIUDAD, TEMP_C) :- 
    temp_f(CIUDAD, TEMP_F),
    TEMP_C is (TEMP_F - 32) * 5/9.