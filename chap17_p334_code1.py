try : 
    text = input("출생년도 입력 : ")
    year = int(text)
    age = 2019 - year + 1
    print("당신은 %d살입니다." % age)
except :
    print("예상치 못한 상황으로 종료합니다.") 
finally :
    print("이용해주셔서 감사합니다. ")
