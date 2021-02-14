import statistics as stat 
scores = [90, 80, 60, 85, 95, 100] 
var = stat.variance( scores ) 
dev = stat.stdev( scores ) 
print( "분산 : " , var)
print( "편차 : " , dev)
