class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other): # 객체의 내용과 내용을 비교해야하는 경우에 연산 메서드를 정의해서 실행해야함
        return self.age == other.age and self.name == other.name  # 이름도 같고 나이도 같아야 같은 객체다 판단할 것임.
#Human() 은 실행 안됨.
kim = Human(29, "김상형")
kim1 = kim # Kim1에 kim을 복제함.
sang = Human(29, "김상형")
moon = Human(44, "김상형")
print(kim == kim1)  # 복제한 내용이기 때문에 이름 나이 모두 같으므로 TRUE
print(kim == sang) # 이름 나이 모두 같으므로 TRUE
print(kim == moon) # 이름 나이 둘 중 하나라도 다르면 FALSE
print("-"*5+"추가"+"-"*5)
dooly = Human(44, "둘리")
print(moon == dooly)  # 이름 다르므로 FALSE
dooly2 = Human(44, "둘리")
print(dooly == dooly2) # 이름 나이 같으므로 TRUE
print(dooly is dooly2) # 동일한 객체를 공유하는 상황인지 물음
print(kim is kim1)  # 두 변수가 동일한 객체를 공유하는 상황에서만 TRUE