import random
import time

맞은개수 = 0 
for t in range (5) : 
    a = random.randint(2,9)
    b = random.randint(1,9)
    dab = a * b
    startTime = time.time( )
    n = int( input( "\n[문제%d]  %d x %d = " % (t+1,a,b) ) )
    endTime = time.time( )
    dTime = endTime - startTime 
    if n==dab :
        if dTime<=2 :                         # 시간제한 : 2초 
            print("시간내에 맞췄습니다.")
            맞은개수 += 1 
        else :
            print("맞췄으나 시간이 초과되었습니다.") 
    else :
        print("땡! 틀렸습니다.")
print("\n당신의 점수는 %d점입니다." % (맞은개수*20) )
