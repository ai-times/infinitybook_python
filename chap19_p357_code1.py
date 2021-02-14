# my_module.py  
pi = 3.14 
e = 2.71 

def info( ) : 
    print("이 모듈은 여러 클래스와 변수를 포함하고 있습니다.") 

class Circle : 
    반지름 = 0 
    def __init__(self, radius) :
        self.반지름 = radius
    def 넓이구하기(self) :
        area = self.반지름 * self.반지름 * 3.14
        print("원의 넓이는", area)

class Square : 
    크기 = 0    
    def __init__(self, size) :
        self.크기 = size
    def 넓이구하기(self) :
        area = self.크기 * self.크기 
        print("정사각형의 넓이는", area)
