try :
    fp = open("d://read_test.txt", "r") 
    for line in fp.readlines() :
        print(line, end="") 
    fp.close()     
except FileNotFoundError :
    print("파일이 존재하지 않습니다.")
finally :
    print("파일 작업 종료합니다.")
