code = input("주민번호 전체 입력 : ")

y = "20" + code[0:2]
m = int( code[2:4] ) 
d = int( code[4:6] )
g = int( code[7:8] ) 

age = 2019-int(y)+1 
print("당신은", y, "년에 태어났군요.")
print("당신의 생일은", m, "월", d, "일 이군요.")
print("당신의 올해", age, "살 이군요")
if g == 3 :
    print("당신은 남성이군요")
else :
    print("당신은 여성이군요")
