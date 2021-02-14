def is_int(n) :
    try:
        int(n)
        return True
    except ValueError :
        return False

def is_float(n) :
    try :
        float(n)
        return True
    except ValueError :
        return False

print( is_int("2002") )             # True 출력
print( is_int("-2002") )            # True 출력
print( is_float("3.14") )           # True 출력 

print( is_int("3.14") )             # False 출력 
print( is_float("2002") )           # True 출력 
