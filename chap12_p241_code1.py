import random

맞은개수 = 0 
for t in range (5) : 
    a = random.randint(2,9)
    b = random.randint(2,9)
    dab = a * b 
    n = int( input( "[문제%d]  %d x %d = " % (t+1,a,b) ) )
    if n==dab :
        맞은개수 += 1 
        print("맞췄습니다.")
    else :
        print("땡! 틀렸습니다.")
print("\n당신의 점수는 %d점입니다." % (맞은개수*20) )
