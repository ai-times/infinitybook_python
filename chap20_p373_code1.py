import random  
import time 

print("=== 주사위 던지기 ===")
print("지금부터 2초에 한번씩 주사위를 던집니다.") 

while 1 : 
    val = random.randint(1, 6)
    print("주사위 값 : %d" % val)
    time.sleep(2)
