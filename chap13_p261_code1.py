import  math 

angle = int( input("각도?"))
dist = int( input("거리?"))  

h = dist * math.tan(  math.radians(angle) )
print("건물의 높이는 %.2f m 입니다." % h )
