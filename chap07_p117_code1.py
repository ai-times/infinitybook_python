print("=== 사각형을 그리는 거북이 ===")
size = int(input("한 변의 길이: "))
import turtle as t

t.shape("turtle")
t.shapesize(3) 

for i in range(4) : 
    t.forward( size )        
    t.right( 90 )


