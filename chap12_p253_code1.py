def  fibo( n ) :   
   if n==1 or n==2:
       return 1
   else :
       return  fibo(n-1) + fibo(n-2) 

while 1 : 
   n = int( input("피보나치 N : ") )
   fb = fibo( n ) 
   print("피보나치(%d) : %d " % (n, fb) )
