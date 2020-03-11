import math
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]



distances = []
for x,y in points:
    distEuc = math.sqrt((x**2) +(y**2))    
    distances.append(distEuc)  
    #cacafuti.append(((x,y), distEuc))

print(min(distances))

pos=0
while (pos < len(points)):
    if distances[pos] == min(distances):
        print (points[pos])
    pos += 1
pos2=0
out = []
while (pos2 < len(points)):
    if distances[pos2] > 9:
        out.append(points[pos2])
    pos2 += 1

print(out)
print(len(out))


#dos maneras distintas de calcular la distancia eúclida
# print(math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)])))

# total = 0
# for a,b in zip(x,y):
#     diferenciaCuadrado = (a - b) ** 2
#     total += diferenciaCuadrado

#print(math.sqrt(total))

