import timeit

def sum1toN( end ) :
    sum = 0 
    for n in range( 1, end+1, 1) : 
        sum += n
    return sum 

number = int(input("몇 까지 더할까요? ")) 
start = timeit.default_timer( )
result = sum1toN( number ) 
end = timeit.default_timer( ) 
    
print( "계산결과 : ", result ) 
print( "수행시간 : ", end - start)
