import turtle as t 
t.shape("turtle") 

t.fillcolor("orange")
t.begin_fill()
t.goto(0, 0) 
t.goto(300, 0)         # 선분1 그리기 
t.goto(300, 300)       # 선분2 그리기 
t.goto(0, 300)         # 선분3 그리기 
t.goto(0, 0)           # 선분4 그리기
t.end_fill()

input()
