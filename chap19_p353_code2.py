class Person :
    name = None
    age = 0
    def 정보입력(self, pName, pAge) :
        self.name = pName
        self.age = pAge

p1 = Person()
p1.정보입력("홍길동", 21)
