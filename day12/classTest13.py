class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):  # 객체의 표현식을 만듦.
        return "이름 %s, 나이 %d" % (self.name, self.age)
    def __len__(self): # 객체의 길이를 조사함.
        return self.age

kim = Human(29, "김상형")
print(kim)
print(len(kim))