var = 100 
def func1( ) :
    global var            # 전역변수 var를 사용할 것을 선언 
    var = 10             # 전역변수 var에 10을 입력
    print("함수1:", var)

func1( )
print("출력1:", var)  
