import statistics

POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
gandalfPower = []
sarumanPower = []

gandalfVictory    = 0
sarumanVictory    = 0

gandalfWins = False
sarumanWins = False

for gandalfSpell,sarumanSpell in zip(gandalf, saruman): 
    
    gandalfPower.append(POWER[gandalfSpell])
    sarumanPower.append(POWER[sarumanSpell])

    if (POWER[gandalfSpell] > POWER[sarumanSpell]):
        gandalfVictory += 1
        if (gandalfVictory == 3 and not sarumanWins):
            gandalfWins = True
    else:
        sarumanVictory += 1
        if (sarumanVictory == 3 and not gandalfWins):
            sarumanWins = True

    # if (gandalfVictory == 3 or sarumanVictory == 3):
    #     break


# for attackGandalf, attackSaruman in zip(gandalf, saruman):
#     gandalfPower.append(POWER[attackGandalf])
#     sarumanPower.append(POWER[attackSaruman])
    

print("Gandalf" if gandalfVictory == 3 else "Saruman", "wins")
print("\tGandalf avg is     ", sum(gandalfPower) / len(gandalfPower))
print("\tSaruman avg is     ", sum(sarumanPower) / len(sarumanPower))
print("\tGandalf stdev is   ", statistics.stdev(gandalfPower))
print("\tSaruman stdev is   ", statistics.stdev(sarumanPower))


print("""\

 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \\
|         _  \ |    ...no sale lo que tiene que salir... algo falla.
 \ \ ,  /      |    Pero lo miraremos pasado mañana
  || |-_\__   /
 ((_/`(____,-'

""")



#statistics.stdev(advance_cm)