# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
import random


# Assign to a list the 3 possible options: 'stone', 'paper' or 'scissors'.
choices=['stone', 'paper', 'scissors']
# Assign a variable to the maximum number of games: 1, 3, 5, etc ...
max_games=3
# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games
to_win=2

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.
def machine_rnd_response():           
    return random.choice(choices)

# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.
def ask_user():
    answer=input('\tStone, Paper or Scissors?: ')

    while(answer not in choices):
        print("\tRespuesta incorrecta, " + answer + " no está permitido")
        answer=input('\tStone, Paper or Scissors?: ')    

    return answer

# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins
def resolve_combat(machine_response, user_resp):
    # print("Nunnakis ha escrito:     ",  user_resp)
    # print("La maquinita ha elegido: ",  machine_response)

    #Variable that represents who wins
    # 2. User wins
    # 1. Machine wins    
    # 0. Tie
    who_wins = 0

    if (machine_response == user_resp):
        who_wins = 0       
    elif (machine_response == "stone" and user_resp == "scissors"):
        who_wins = 1
    elif (machine_response == "scissors" and user_resp == "paper"):
        who_wins = 1       
    elif (machine_response == "paper" and user_resp == "stone"):
        who_wins = 1       
    else:       
        who_wins = 2
   
    return who_wins
    # if (who_wins == 0):
    #     winner = "Tie"
    # elif (who_wins == 2):
    #     winner = "User wins"
    # else:
    #     winner = "Machine wins"    
    #print(winner + " (" + machine_response + ") - ("+ user_resp + ")")



print("EL JUEGO DE PIEDRA PAPEL Y TIJERARRRR")
print("*************************************")
# Create two variables that accumulate the wins of each participant


print("Comienza el juego")
machine_total_wins = 0
user_total_wins = 0

for game in range(0, max_games):       
    print("\tJuego número: ", game)
    machine_points = 0
    user_points = 0

    while (machine_points <= 2 and user_points <= 2):

        round_winner = resolve_combat( machine_rnd_response() , ask_user() )
        if (round_winner == 1):                   
            machine_points += 1
            print("\t\t\tMachine wins the round (" + str(machine_points) + " en el game " + str(game) + ")")
        elif( round_winner == 2):
            user_points += 1
            print("\t\t\tNunakkis wins the round (" + str(user_points) + " en el game " + str(game)+ ")")
        else:
            print("Tie.")
        
    if (machine_points > user_points):
        print("\t\tMachine wins (" + str(game) + ")")
        machine_total_wins += 1
    else:
        print("\t\tNunakki wins (" + str(game) + ")")  
        user_total_wins += 1




# if (machine_points > user_points):
#     print("Machine wins")
# elif (machine_points < user_points):
#     print("nunakkis wins")
# else:
#     print("Tie")




#combat( machine_response(), ask_user())

    # Preguntamos a usuario su jugada
    # Preguntamos a la máquina su jugada
    # Comparamos la jugada de la máquina (jugadaMaquina) con la del usuario (jugadaUsuario)
    # Si jugadaMaquina es Tijeras Y jugadaUsuario es Papel, g



# Repetiremos tantas veces como max_games
    # Repetiremos tantas veces como to_win






    
# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated

    



# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.

    
# Print by console the winner of the game based on who has more accumulated wins