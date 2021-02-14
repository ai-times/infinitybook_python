import math

a = int(input("a 값? "))
b = int(input("b 값? "))
c = int(input("c 값? "))
판별식 = b**2 - 4*a*c 

if 판별식 <0 :
    print("해가 없습니다.") 
elif 판별식 == 0 :
    print("해가 1개 입니다.")
    print("해 : %.2f" % (-b/2*a) )
elif 판별식 > 0 : 
    해1 = (-b + math.sqrt(판별식)) /  (2*a)
    해2 = (-b - math.sqrt(판별식)) /  (2*a) 
    print("해1: %.2f, 해2: %.2f" %(해1,해2) )
