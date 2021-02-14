from datetime import date 

year = int( input("몇 년도에 태어났나요? ") ) 
month =int( input("몇 월에 태어났나요? ") ) 
day = int( input("몇 일에 태어났나요? ") )

birthday = date( year, month, day ) 
today = date.today( )
dur = today - birthday
print("당신이 살아온 날 수 : ", dur.days )
