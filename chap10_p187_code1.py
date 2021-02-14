def myFunc( x ) :                       # 함수 정의 
    result = x**2 + 5*x + 3     
    return result 

# 여기서부터 실행됨 
x = 10 
y = myFunc( x )                         # 함수 호출 
print( "f(%d) = %d" % (x, y) )
