fp = open("exam.txt", "r")
for line in fp.readlines( ) : 
    print( line, end="" )
fp.close( )
