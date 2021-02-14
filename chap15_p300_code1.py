scores = [ ] 
for i in range(5) :
    value = int( input("성적입력 : ") )
    scores.append(value) 

print(scores)                       # 입력 받은 리스트 출력 

sum = 0 
for i in range(5) :
    sum += scores[i] 
print("합계: ", sum)
print("평균: ", (sum/5)) 
