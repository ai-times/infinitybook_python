Start = int(input("몇 부터 더할까요? ")) 
End = int(input("몇 까지 더할까요? ")) 

sum = 0
for n in range (Start, End+1, 1) :
    sum += n 

print("%d부터 %d까지 더한 값은 %d 입니다." % (Start, End, sum)) 
