import turtle as t 

t.penup()
t.goto(0,0);    t.write(" (0,0)")
t.goto(0,200);  t.write("(0,200)")
t.pendown()
t.goto(0,-200); t.write(" (0,-200)")

t.penup()
t.goto(-200,0);  t.write("(-200,0)")
t.pendown()
t.goto(200,0); t.write(" (200,0)")
t.penup()

t.goto(-150,-150)
t.pendown()
t.color("blue")
t.goto(150,150);    t.write("y=x")
t.goto(0,0)
t.penup() 



