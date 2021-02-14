while 1: 
    query = input("\n프로그래밍 언어 입력: ")
    query = query.lower() 
    if "c" in query :
        print("C언어는 1972년에 태어났어요.")
    elif "java" in query :
        print("Java언어는 1995년에 태어났어요.")
    elif "python" in query :
        print("Python은 1991년에 태어났어요.")
    elif "go" in query :
        print("Python은 2009년에 태어났어요.")
    elif "pascal" in query :
        print("Pascal은 1969년에 태어났어요.")
    else :
        print("등록되지 않은 언어입니다.")
