def func1( param ) :          # 지역변수 param
    var = 10 * param         # 지역변수 var 
    print("함수1:", param)

func1( 5 ) 
print("출력1:", var)             # 에러 발생 
print("출력2:", param)          # 에러 발생
