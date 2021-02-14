import turtle as t

def 사각형(x, y) :
    t.goto(x,y)
    t.pendown()
    for i in range (4) :
        t.forward(100)
        t.left(90)
    t.penup()
    return 0


t.shape("turtle")
t.penup() 

사각형(0,0)
사각형(150,0)
사각형(300,0)

사각형(0,150)
사각형(150,150)
사각형(300,150)


