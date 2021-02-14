a = int(input("두 수 중 작은 수 A : "))
b = int(input("두 수 중 큰 수 B : "))
while 1:
    if a==b :
        print("최대공약수 : ", a)
        break 
    else :
        if a>b :
            a = a - b
        else :
            b = b - a
print("종료합니다.") 
