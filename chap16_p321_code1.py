dic = {'c':1972, 'java':1995, 'python':1991, 'go':2009, 'pascal':1969 }
while 1: 
    query = input("\n프로그래밍 언어 입력: ")
    key = query.lower() 
    year = dic.get( key ) 
    print("{}언어는 {}년에 태어났어요.".format(query, year) )
