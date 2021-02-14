from datetime import date 
d1 = date(2002, 6, 30)                          # 생일 입력 
d2 = date(2021, 2, 11)                         # 오늘 날짜, today() 적합 
dur = d2 - d1
print("당신은 태어나서 %d일 살았군요 " % dur.days ) 
print( type(dur) ) 
