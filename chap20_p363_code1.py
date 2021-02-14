import time
startTime = time.time( ) 
for i in range(100) : print("count", (i+1) )        # 1부터 100까지 출력하기 
endTime = time.time( ) 
print("수행시간 : ", (endTime-startTime) ) 
