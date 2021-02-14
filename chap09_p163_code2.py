from datetime import date

today = date.today() 

birthYear = int(input("몇 년도에 태어났나요? "))
age = today.year - birthYear + 1

if age>=15 and age<20 :
    print("당신은 청소년입니다.")
print("올해 당신은 %d살입니다." % age)

# 실행 후 2005 라고 입력해보자. 
print() 
