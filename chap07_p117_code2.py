import turtle as t
t.shape("turtle")
t.shapesize(3) 

temp = t.textinput("사각형", "한 변의 길이: ")
size = int(temp) 

for i in range(4) : 
    t.forward( size )        
    t.right( 90 )


