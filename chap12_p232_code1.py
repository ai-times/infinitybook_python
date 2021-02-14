print("팩토리얼 값 계산 프로그램")
n = int(input("정수 입력: "))

fact = 1
for i in range(1, n+1) :
    fact*= i

print("계산결과 %d! = %d" % (n,fact))
input() 
