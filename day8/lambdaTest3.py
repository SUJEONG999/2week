def calc():
    num  = 100
    return lambda : num + 1    # 람다 표현식을 반환  , 리턴 값 뒤의 함수 수행은 계속 유지됨.

c1 = calc()
print(c1(), c1(), c1())   # 클로저가 일어나서 호출할 때마다 101이 호출됨


def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환  # a,b 모두 유지가 됨.

c2 = calc()
print(c2(1), c2(2), c2(3), c2(4), c2(5))


def calc():  # outer함수
    a = 3
    b = 5
    def expr(x) :    #함수안의 함수로(inner 함수)
        return a * x + b

    return expr

c3 = calc()
print(c3(100), c3(200), c3(300), c3(400), c3(500))


