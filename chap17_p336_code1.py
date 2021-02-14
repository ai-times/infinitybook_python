try :
    t = input("정수 입력:")) 
    n = int( t ) 
    m = 100 / n
    print("100을 %d으로 나눈 몫 : %d" % (n,m))
    print("입력한 두번째 숫자 : %c" % t[1]) 
except  :
    print("예상치 못한 상황으로 종료합니다.")
