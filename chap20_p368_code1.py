from datetime import date 

print("=== 생후 몇일 계산 프로그램 ===")
birthYear = int(input("몇 년도에 태어났나요? "))
birthMonth = int(input("몇 월에 태어났나요? "))
birthDay = int(input("몇 일에 태어났나요? "))

생일 = date( birthYear, birthMonth, birthDay)
오늘 = date.today()
생후일수 = (오늘-생일).days  

print("생후 %d 일" % 생후일수 )
