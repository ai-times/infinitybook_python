성적 = int(input("시험점수 입력 : "))
결석 = int(input("결석회수 입력 : "))

if 성적>=70 and 결석<3 :
    print("Pass했습니다. 축하합니다.")
elif 성적>=50 and 성적<70 and 결석<3 : 
    print("재시험 가능자입니다.") 
else :
    print("Fail입니다. ")
