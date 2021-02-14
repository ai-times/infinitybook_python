fibo = [1, 1]

index = 2 
while index<=100 :
    fibo.append( fibo[index-1] + fibo[index-2] )
    index += 1

while True : 
    n = int(input("피보나치 수열의 몇 번째 값을 구해줄까요? "))
    result = fibo[n-1] 
    print("피보나치 수열 %d번째 값 : %d \n" %(n, result) )
