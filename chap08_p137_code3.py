print("== 몸무게 제안 프로그램 ===") 
height = float( input( "키 입력 -> " ))
weight = (height - 100) * 0.9
print("키 %.1f cm에 대한 적정몸무게는 %.1f kg입니다." % (height, weight))

input() 
