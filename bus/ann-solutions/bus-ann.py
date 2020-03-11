import math
import statistics

def absolute(numero):
    if (numero > 0):
        return numero
    else:
        return numero * -1



stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

numStops = len(stops)

numPass = []
devList = []
totalPass = 0


for stopIn, stopOut in stops:
    totalPass += (stopIn-stopOut)
    
    numPass.append(totalPass)
print(numPass)

avg = sum(numPass) / len(numPass)
print(avg)
for dev in numPass:
    dev -= avg
    devList.append(dev**2)

# print(devList)
print(len(devList))
print(statistics.stdev(numPass))
print("Std deviation =", math.sqrt(sum(devList) / (len(devList) - 1)))

