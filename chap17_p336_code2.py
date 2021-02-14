try :
    t = input("정수 입력: ") 
    n = int( t ) 
    m = 100 / n
    print("100을 %d으로 나눈 몫 : %d" % (n,m))
    print("입력한 두번째 숫자 : %c" % t[1]) 
except ValueError :                         # 3.14 입력 
    print("예외상황: 값변환 오류")
except ZeroDivisionError :                   # 0 입력
    print("예외상황: 0으로 나눈 오류")
except IndexError :                         # 6번 라인 발생
    print("예외상황: 인덱스 범위 오류")
