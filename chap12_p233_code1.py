print("팩토리얼 값 계산 프로그램")
n = int(input("정수 입력: "))
i = 1 
fact = 1
while i<= n :
    fact *= i
    i += 1 
print("계산결과 %d! = %d" % (n,fact))
input() 
