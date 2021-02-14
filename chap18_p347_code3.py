var = 100
def func1( ) :
    var = 10
    print("함수1:", var)
def func2( ) :
    global var
    var = 10
    print("함수2:", var) 

print("출력1:", var)
func1( )
print("2차:", var)
func2( )
print("3차:", var)
