import operator

print("Programa super awesome del caracol y el pozo")
print("********************************************")

print("""\


         __,._
        /  _  \                                    
       |  6 \  \  oo                            
        \___/ .|__||                             
 __,..="^  . , "  , \   ---> Soy el caracol del programa. Me llamo Pepe                           
<.__________________/

""")




well_height    = 125
snail_rise     = 30
snail_slide    = 20

snail_location = 0
total_days     = 0
is_daytime     = False

while (snail_location <= well_height):
    is_daytime = operator.not_(is_daytime)
    if (is_daytime):
        snail_location += snail_rise
        total_days += 1
    else:
        snail_location -= snail_slide
    #print("Día:" if is_daytime else "Noche:" , total_days, ". El caracol está a ", snail_location)

print("Pepe ha salido el día: ", total_days)
    


