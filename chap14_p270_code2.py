text = input("출생년도 입력? ")
if text.isdecimal() == True :
    year = int( text )
    age = 2019 - year + 1 
    print("당신은 %d살입니다." % age)
else :
    print("출생년도 입력 오류입니다.")
