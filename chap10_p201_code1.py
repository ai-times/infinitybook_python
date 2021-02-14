import turtle as t

def rectangle(x, y) :
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.fillcolor( "green" ) 
    for i in range (4) :
        t.forward(100)
        t.left(90)
    t.end_fill() 
    t.penup()
    return 0

t.shape("turtle")
t.penup() 
rectangle(0,0)
rectangle(150,0)
rectangle(300,0)

