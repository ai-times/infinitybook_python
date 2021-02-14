import time
startTime = time.time( ) 
sum = 0 
for n in range (1, 10000001, 1) : 
    sum += n 
endTime = time.time( ) 
print("결과 : ", sum) 
print("수행시간 : %.3f초" % (endTime-startTime) )
