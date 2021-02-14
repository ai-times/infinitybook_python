hlist = list( range(150,181,3) )
wlist = [ (h-100)*0.9 for h in hlist ]

for i in range( len(hlist) ) :
    print("{0:2d} {1:5d}cm {2:6.1f}kg".format(i+1, hlist[i], wlist[i]) ) 
