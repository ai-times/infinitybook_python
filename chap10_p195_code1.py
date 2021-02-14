import math 

def sine(각도) :
    if 각도==0 :
        return 0
    elif 각도==30 :
        return 1/2
    elif 각도==45 :
        return math.sqrt(2)/2
    elif 각도==60 :
        return math.sqrt(3)/2
    elif 각도==90 :
        return 1

print( "30도: %.2f" % sine(30) )
print( "45도: %.2f" % sine(45) )
print( "60도: %.2f" % sine(60) )
