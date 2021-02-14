fibo = [1, 1]

index = 2 
while index<=10 :
    fibo.append( fibo[index-1] + fibo[index-2] )
    index += 1

print( fibo )             # 리스트 전체를 출력해줍니다. 
