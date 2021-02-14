def 원의둘레구하기(반지름) :
    pi = 3.141592
    원의둘레 = 2*반지름*pi
    return 원의둘레 

def 원의넓이구하기(반지름) :
    pi = 3.141592
    원의넓이 = 반지름*반지름*pi
    return 원의넓이 
    
n = int(input("원의 반지름 입력 : "))
result1 = 원의둘레구하기( n )
result2 = 원의넓이구하기( n )
print("원의 둘레 : %.2f " % result1)
print("원의 넓이 : %.2f " % result2) 

