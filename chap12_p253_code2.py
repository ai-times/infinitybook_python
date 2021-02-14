import   math 

while 1 :
    n = int(input("양의 정수 N : "))
    result1 = 1/math.sqrt(5) * math.pow((1+math.sqrt(5))/2, n)
    result2 = 1/math.sqrt(5) * math.pow((1-math.sqrt(5))/2, n)
    result = result1 - result2 
    print("답은 : %d " % result)
