def fct_fac(n) :  # 함수 안에 함수를 또 넣을 수 있음.
    def exp(x) :   # exp함수는 이 함수 안에서만 호출가능함.
        return x**n
    return exp

rtnf1 = fct_fac(2)
rtnf2 = fct_fac(3)

print(type(rtnf1))
print(type(rtnf2))

print(rtnf1(4))  # 4의 2승
print(rtnf2(4))  # 4의 3승
