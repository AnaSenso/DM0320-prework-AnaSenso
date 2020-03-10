gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
gandalf_win = 0
saruman_win = 0

# para cada ataque en la lista de ataques 
    # mira el valor de la posicion (también llamada ataque) de gandalf y saruman y dime cual es mayor
        # incrementa en 1 el xxx_win del ganador
# si gandalf_win > saruman_win
    #imprime Gandalf gana
# si no:
    # imprime Saruman gana



paquetitos = zip(gandalf, saruman)

for gandalfAttack,sarumanAttack in paquetitos:
    if (gandalfAttack > sarumanAttack):
        gandalf_win += 1
    else:
        saruman_win += 1    






"""

#Hacerlo con while
posicionAtaque = 0
while(posicionAtaque < len(gandalf)):
    if (gandalf[posicionAtaque] > saruman[posicionAtaque]):
        gandalf_win += 1
    else:
        saruman_win += 1
    posicionAtaque += 1






#Hacerlo con for raro
ataqueInicial = 0
for ataque in gandalf:
    
    #if (gandalf[ataqueInicial] > saruman[ataqueInicial]):
    if (ataque > saruman[ataqueInicial]):
        gandalf_win += 1
    else:
        saruman_win += 1
    ataqueInicial += 1

if (gandalf_win > saruman_win):
    print("Gandalf es el mejor")
else:
    print("Saruman es un tramposo")


"""