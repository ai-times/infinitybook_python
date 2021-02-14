Import timeit 
start = timeit.default_timer( )  
sum =0 
for n in range( 1, 10001, 1) : 
    sum += n 
end = timeit.default_timer( ) 
print( "계산결과 : ", sum) 
print( "수행시간 : ", end - start) 
