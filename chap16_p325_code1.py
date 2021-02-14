dic = { } 
fp = open("animal_eng.txt", "r")
for line in fp.readlines() :
    x = line.split(",")         
    dic[x[0]] = x[1].replace("\n","").replace(" ","")  
fp.close()
# print(dic)                  # 완성된 딕션너리를 확인하는 코드

while 1: 
    query = input("\n동물 이름(한글) : ")
    key = query.lower()
    if key in dic : 
        eng = dic.get(key)
        print("{}는 영어로는 {}입니다.".format(query, eng) )
    else : 
        print("등록되지 않은 언어입니다.")
