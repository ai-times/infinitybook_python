class Circle :                     # 클래스 이름 시작은 대문자 권장 
    반지름 = 0 
    def 반지름정하기(self, radius) :
        self.반지름 = radius
    def 넓이구하기(self) :
        area = self.반지름 * self.반지름 * 3.14
        print("원의 넓이는", area)

c1 = Circle()
c1.반지름정하기(10) 
c1.넓이구하기()
