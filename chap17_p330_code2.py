fp = open( "d:\\구구단5단.txt", "w" ) 
for t in range ( 1, 10, 1) : 
    fp.write("5 x %d = %d \n" % (t, 5*t) ) 
fp.close( ) 
print("구구단 5단이 파일(d:\\구구단5단.txt)에 출력되었습니다.")
