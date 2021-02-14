class Person :
    name = None
    age = 0
    def 정보입력(self, pName, pAge) :
        self.name = pName
        self.age = pAge
    def 자기소개(self) :
        print("안녕하세요")
        print("내 이름은 ", self.name, "입니다.")
        print("나이는", self.age, "살입니다.") 

p1 = Person()
p1.정보입력("홍길동", 21)
p1.자기소개()
