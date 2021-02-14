class Circle :     
    반지름 = 0 
    def 반지름정하기(self, radius) :
        self.반지름 = radius
    def 넓이구하기(self) :
        area = self.반지름 * self.반지름 * 3.14
        print("원의 넓이는", area)
def 둘레구하기(self) :
        area = 2* self.반지름 * 3.14
        print("원의 둘레는", area)

c1 = Circle()
c1.반지름정하기(10) 
c1.넓이구하기()
c1.둘레구하기()
