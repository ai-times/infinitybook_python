import calendar

print("당신이 태어난 달의 달력을 보여줄께요.\n") 
year = int( input("몇 년도에 태어났어요? ") )
month = int( input("몇 월에 태어났어요? ") ) 

print("\n당신이 태어난 달의 달력입니다.\n") 
달력 = calendar.month(year, month)
print(달력) 
