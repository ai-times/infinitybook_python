# 모든 멤버 함수는 파라미터로 self 가 첫번째로 입력되어야 한다. 
class Circle :     # 클래스 이름은 대문자로 시작
    r = None
    def __init__(self, radius=20) :
        print("Circle 객체가 생성됩니다.")
        self.r = radius 
    def setR(self, radius) :
        self.r = radius
    def 넓이구하기(self) :
        area = self.r * self.r * 3.14
        print("원의 넓이는", area)
    def 둘레구하기(self) :
        line = 2 * self.r * 3.14
        print("원의 둘레는", line)        

c1 = Circle()
print(c1.r) 
c1.setR(10)
print(c1.r) 
c1.넓이구하기()
c1.둘레구하기()
