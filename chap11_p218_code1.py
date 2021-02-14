End = int(input("몇 까지 더할까요? ")) 

sum = 0
for n in range (1, End+1, 1) :
    sum += n 

print("1부터 %d까지 더한 값은 %d 입니다." % (End, sum) )
