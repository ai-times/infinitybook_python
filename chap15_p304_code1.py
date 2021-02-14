import math as m
import turtle as t

xlist = list( range(0,721,10))
ylist = [ m.sin(m.radians(x)) for x in xlist ]

for i in range(len(xlist)) :
    x = xlist[i]
    y = ylist[i]
    t.goto(x/1.6,y*150)                     # 그래프 그리기 
    print("%3d도 --> %6.2f" % (x,y))        # 값 출력하기 

