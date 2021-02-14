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

t.shape("turtle")
t.penup() 
t.speed(10)
for y in range(-300, 300, 120) :
    for x in range(-300, 300, 120) :
        rectangle(x, y)
