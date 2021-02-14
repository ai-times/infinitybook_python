print("구구단을 알려줄께요.")
n = int(input("구구단 몇 단을 알려줄까요? "))

for i in range (2, 10, 1) :
    print("%d x %d = %d " % (n, i, n*i) )
