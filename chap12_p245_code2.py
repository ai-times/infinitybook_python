def 소수판별함수(n) : 
    success = True 
    for t in range( 2, n, 1) :
        if n%t == 0 :
            return False
    return True 

n = int(input("어떤 수를 판별해줄까요? "))
result = 소수판별함수( n )
if result==True :
    print("소수입니다.")
else :
    print("소수가 아닙니다.")
