n = int(input("어떤 수를 판별해줄까요? "))
success = True
for t in range (2, n, 1) : 
    if n%t == 0 :
        success = False
        break 

if success == True :
    print("소수 입니다.")
else :
    print("소수가 아닙니다.")
