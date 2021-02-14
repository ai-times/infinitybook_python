import turtle as t

t.width(3)
t.shape("turtle") 

# n = int(input("몇 각형을 그려줄까요?"))
n = int( t.textinput("다각형", "몇 각형을 그려줄까요?")) 

for i in range ( n ) :            
    t.forward( 200 )        
    t.right( 360/n )           
