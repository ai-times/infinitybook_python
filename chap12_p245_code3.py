def 소수판별함수(n) : 
    success = True 
    for t in range( 2, n, 1) :
        if n%t == 0 :
            return False
    return True 

소수개수 = 0 
합계 = 0 
for t in range (2, 51, 1) :
    if 소수판별함수(t)==True :
        print("%d는 소수입니다." % t)
        소수개수 += 1
합계 += t

print("소수개수 : ", 소수개수)
print("모든 소수의 합계 : ", 합계)
