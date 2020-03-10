avancedia  = 30
retronoche = 20
distancia  = 0
dias       = 0
altura     = 125

advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

#Cuántos días tarda?
#Mientras la distancia es menor que la altura
    # Hazme días + 1
    # Si avanzas 30 y no sales, retrocedes 20

# while(distancia < altura):
#     distancia += avancedia
#     dias += 1
#     if (distancia < altura):
#         distancia -= retronoche

# print("Days:", dias)

while (distancia <= altura):
    distancia += advance_cm[dias]
    print("Día :", dias, ". Distancia :", distancia)
    dias += 1
    if (distancia <= altura):
        distancia -= retronoche

print(dias)

