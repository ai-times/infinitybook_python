키 = int(input("키가 몇 cm 에요? "))
몸무게 = int(input("몸무게가 몇 kg이에요"))
미터키 = 키/100
bmi = 몸무게 / 미터키**2
print("당신의 BMI : %.2f " %  bmi)

if bmi >= 40 : 
   print("고도비만입니다.") 
   printf("매우 심각한 비만이니 의사와 상담하세요.") 
elif bmi >=30 : 
   print("비만입니다.") 
   print("심각한 비만이니 식사량을 줄이고 주 2회 이상 운동을 하세요") 
elif bmi >=25 : 
   print("경도비만입니다.") 
   print("약한 비만 단계입니다. 주 2회 이상 꾸준히 운동하면 금방 정상인이 됩니다.") 
elif bmi >=20 : 
   print("정상체중입니다.") 
else : 
print("저체중입니다.")
print("식사를 제때에 충분히 하고 근육 운동을 하세요") 
