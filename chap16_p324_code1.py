dic = { } 
fp = open("animal_eng.txt", "r")
for line in fp.readlines() :
    x = line.split(",")         
    dic[x[0]] = x[1].replace("\n","").replace(" ","")  
fp.close()
# print(dic)                  # 완성된 딕션너리를 확인하는 코드 
