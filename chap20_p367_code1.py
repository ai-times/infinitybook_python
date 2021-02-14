from datetime import date 
week = [ '월', '화', '수', '목', '금', '토', '일' ]

year = int(input("몇 년도에 태어났나요? ")) 
month =int(input("몇 월에 태어났나요? ")) 
day = int(input("몇 일에 태어났나요? "))
birthday = date( year, month, day )

print( birthday.isoformat(), "에 태어난 당신") 
index = birthday.weekday() 
print( week[index], "요일에 태어났군요", sep='' )
