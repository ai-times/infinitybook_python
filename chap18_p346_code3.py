var = 100                    # 전역변수 var 

def func1( ) :
    var = 10                   # 지역변수 var
    print("함수1:", var)

func1( )
print("출력1:", var)  
