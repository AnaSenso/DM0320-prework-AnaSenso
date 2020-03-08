POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']


gandalfVictory = 0
sarumanVictory = 0

for gandalf,saruman in zip(gandalf, saruman):  
    print(POWER[gandalf], POWER[saruman])
    if (POWER[gandalf] > POWER[saruman]):
        gandalfVictory += 1
    else:
        sarumanVictory += 1
