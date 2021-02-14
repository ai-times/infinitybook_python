fp = open("d:\\구구단-전체.txt", "w")
fp.write("구구단 전체 출력 프로그램\n") 
for n in range (2, 10, 1) : 
    fp.write("\n구구단 %d 단 출력 \n" % n )  
    fp.write("--------------------\n")  
    for t in range ( 1, 10, 1) : 
        fp.write("%3d x %3d = %3d \n" % (n, t, n*t) )
print("구구단 전체가 파일에 출력되었습니다.") 
fp.close( )
