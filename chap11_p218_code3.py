import sys

Start = int(input("몇 부터 더할까요? ")) 
End = int(input("몇 까지 더할까요? ")) 

if Start > End :
    print("시작하는 수가 끝나는 수보다 크면 안됩니다.") 
    sys.exit( )
    
sum = 0
for n in range (Start, End+1, 1) :
    sum += n 

print("%d부터 %d까지 더한 값은 %d 입니다." % (Start,End,sum))
