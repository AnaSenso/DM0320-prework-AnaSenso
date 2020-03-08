import operator
import statistics


well_height    = 125
advance_cm     = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
snail_location = 0
total_days     = 0
snail_slide    = 20
is_daytime     = False

while (snail_location <= well_height):
    is_daytime = operator.not_(is_daytime)
    if (is_daytime):
        snail_location += advance_cm[total_days]
        total_days += 1
    else:
        snail_location -= snail_slide
    #print("Día:" if is_daytime else "Noche:" , total_days, ". El caracol está a ", snail_location)


"""
Standard deviation

1. Work out the Mean (the simple average of the numbers)
2. Then for each number: subtract the Mean and square the result.
3. Then work out the mean of those squared differences.
4. Take the square root of that and we are done!

"""


average = sum(advance_cm) / len(advance_cm)

print("El caracol salió el día:" , total_days, " :)" )
print("\tSubió como máximimo   :", max(advance_cm))
print("\tSubió como mínimo     :", min(advance_cm))
print("\tLa media de subida es :", average)
print("\tLa desviación es      :", statistics.stdev(advance_cm))