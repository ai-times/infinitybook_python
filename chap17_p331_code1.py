fp = open("read_test.txt", "r")
while 1 :
    line = fp.readline()
    if len(line)==0 :
        break 
    print( line, end="" ) 
fp.close( )
