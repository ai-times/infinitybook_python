import math

a = int(input("a 값? "))
b = int(input("b 값? "))
c = int(input("c 값? "))
판별식 = b**2 - 4*a*c 
해1 = (-b + math.sqrt(판별식)) / (2*a)
해2 = (-b - math.sqrt(판별식)) / (2*a) 

print("해1: ", 해1)
print("해2: ", 해2)
