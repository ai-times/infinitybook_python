dic = {} 
fp = open("prog_lang.txt", "r")
for line in fp.readlines() :
    x = line.split(",")             # x는 2개 항목으로 된 리스트 
    dic[x[0]] = int(x[1])          # x[0]는 언어, x[1]은 년도 정보 
fp.close()                       
print(dic)                       # 딕션너리 구성 확인 

