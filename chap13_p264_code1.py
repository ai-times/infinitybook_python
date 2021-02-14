import math as m

for t in range (0, 361, 15) :
    val = m.sin( m.radians(t) ) 
    print("각도: %3d, 싸인값 : %.2f" % (t, val) )

