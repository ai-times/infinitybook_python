curHour = int( input("지금 몇시인가요? ") ) 
prevHour = curHour - 6
if prevHour < 0 :
    prevHour += 24 
print("현재 시간 : %d시" % curHour)
print("이전 시간 : %d시" % prevHour)
