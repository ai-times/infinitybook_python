print("구구단을 알려줄께요.")
while True : 
    n = int(input("구구단 몇 단을 알려줄까요? "))
    if 2<=n<=9 : 
        break 
    else : 
        print("2~9 사이의 정수만 입력 가능합니다.\n") 
    
for i in range (1, 10, 1) :
    print("%d x %d = %d " % (n, i, n*i) )
