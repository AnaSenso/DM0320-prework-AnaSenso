def alarma(counter):
    moment=[]
    pos=0
    bleep = 0
    while (pos < len(dbs)):
        if dbs[pos] > 10:
            bleep+=1
            if bleep >= counter:
                print("Alarm")
            moment.append(pos)
        else:
            bleep = 0
        pos+=1



dbs = [20, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 
       1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 11, 1110]

# noise=[]
# db=0

# while (db < len(dbs)):
#     if dbs[db] > 10:
#         noise.append(dbs[db])
#     db +=1

# print(noise)



alarma(4)



# while (pos < len(dbs)):
#     if dbs[pos] > 10:
#         bleep+=1
#         if bleep >= 3:
#             print("Alarm")
#         moment.append(pos)
#     else:
#         bleep = 0
#     pos+=1

# print(moment)

# seguidos=0
# while (seguidos < len(moment)):
#     if (moment[seguidos])+1 == (moment[seguidos+1]):
#         print("Alarm!")
#         break
#     seguidos+=1

# where=[]
# for pos,db in list(enumerate(dbs)):
#     if db > 10:
#         where.append((pos,db))

# print(where)  

#print(list(enumerate(dbs)))
