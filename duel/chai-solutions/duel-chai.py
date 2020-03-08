gandalfAttacks = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
sarumanAttacks = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

gandalfVictory = 0
sarumanVictory = 0

for gandalf,saruman in zip(gandalfAttacks, sarumanAttacks):  
    if (gandalf > saruman):
        gandalfVictory += 1
    else:
        sarumanVictory += 1

print(gandalfVictory)
print(sarumanVictory)

print("Gandalf" if gandalfVictory > sarumanVictory else "Saruman", "wins")