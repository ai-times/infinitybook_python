import turtle as t 
import random
import time 

t.shape("turtle")
t.shapesize(3) 

while 1 :
    x = random.randint(-300, 300) 
    y = random.randint(-300, 300)
    size = random.randint(30, 100)

    t.penup() 
    t.goto(x, y)
    t.pendown()
    t.circle(size)
    time.sleep(0.3)
