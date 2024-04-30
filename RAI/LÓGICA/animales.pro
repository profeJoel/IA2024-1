animal(coyote).
animal(elefante).
animal(pudu).
animal(oso).
animal(panda).
animal(guacamayo).
animal(rinoceronte).
animal(carpincho).
animal(lobo).
animal(dragon_de_comodo).

mas_grande(elefante,rinoceronte).
mas_grande(rinoceronte, oso).
mas_grande(dragon_de_comodo,guacamayo).
mas_grande(panda, pudu).
mas_grande(lobo, coyote).
mas_grande(pudu, carpincho).
mas_grande(oso, carpincho).
mas_grande(panda, dragon_de_comodo).
mas_grande(carpincho, guacamayo).


mas_grande(A1,A2):- mas_grande(A1, X), mas_grande(X, A2).