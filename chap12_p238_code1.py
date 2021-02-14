import winsound 
print("369게임 시작") 
n=1 
while n <= 35 :
    if n%3 == 0 or "3" in str(n) : 
        print( "박수" )
    else : 
        print( n ) 
    n = n + 1
    winsound.Beep(700, 500) 
print("369게임 끝")
