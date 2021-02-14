import random

a = random.randint(2,9)
b = random.randint(2,9)
dab = a * b 

n = int( input( "%d x %d = " % (a,b) ) )
if n==dab :
    print("맞췄습니다.")
else :
    print("땡! 틀렸습니다.")
