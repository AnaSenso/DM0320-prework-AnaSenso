POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']


# POWER[ataque]
# Para cada ataque en la lista de ataques de Gandalf y Saruman
    # Si el valor de ataque en el diccionario en la lista de Gandalf es mayor al valor de ataque en la lista de Saruman -> +1 Gandalf_wins
    # else +1 saruman_wins
gandalf_wins = 0
saruman_wins = 0
posicion = 0

while(posicion < len(gandalf)):    

    if(POWER[gandalf[posicion]] > POWER[saruman[posicion]]):
        gandalf_wins += 1
    else:
        saruman_wins += 1
    posicion += 1

print("Gandalf es el mejor" if gandalf_wins > saruman_wins else "Saruman eres un tramposo")




