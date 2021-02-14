dic = {} 
fp = open("prog_lang.txt", "r")
for line in fp.readlines() :
    x = line.split(",")          # x는 2개 항목으로 된 리스트
    dic[x[0]] = int(x[1])       # x[0]는 언어, x[1]은 년도 정보 
fp.close()

while 1 : 
    query = input("\n무엇이 궁금하세요? ")
    query = query.lower() 

    for key in dic.keys() :
        if key in query : 
            year = dic.get(key)
            print("{}언어는 {}년에 태어났어요".format(key,year) )
            break 
    else : 
        print("제가 이해할 수 없는 질문입니다.")
