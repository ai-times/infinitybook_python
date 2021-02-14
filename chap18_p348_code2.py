def func1( ) :
    global var 
    var = 10  
    print("함수1:", var)

def func2( ) :
    global var 
    var += 3
    print("함수2:", var) 

func1( )
func2( )
var += 5 
print("출력1:", var)

