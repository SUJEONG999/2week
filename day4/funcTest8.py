def add(num1, num2) :
    print(num1 + num2)   # 리턴 값이 없고, none이 리턴됨

r1 = add(10, 20)   # 30 출력됨
v1 = 100; v2 = 200
r2 = add(v1, v2)  # 300 출력됨
print(r1)  # none이 리턴됨
print(r2)  #none이 리턴됨
print(add(1000, 2000))  # 3000출력되고, none 출력
print(1+bool(add(1000, 2000)))   # 3000출력되고, 1출력(bool은 참이면1, 거짓0)
print(1+add(1000, 2000))
