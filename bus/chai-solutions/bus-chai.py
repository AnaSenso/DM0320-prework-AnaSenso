stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

print("Stops: ", len(stops))
passageIn,passageOut = zip(*stops)

print (*passageIn)

maximumOcuppation = 0

total = 0

for passageIn,passageOut in stops:    
    #total += passageIn - passageOut

    if (total > maximumOcuppation):
        maximumOcuppation = total

print ("Max is: ", maximumOcuppation)
print ("Avg is: ", total / len(stops), total)
# ^^^ 
# esto falta por afinarlo





""" 
Más maneras de pintar una array
    
    a = [1, 2, 3, 4, 5] 

    //en bucle
    for x in range(len(a)): 
    print a[x], 
    
    //haciendo join a la string
    print(' '.join(map(str, a)))  
  
    //Asterisco sirve para pintar todos los elementos de la array
    //El separador es opcional, para separar por comas o lo que se quiera
    print(*a, sep = ", ")  


"""