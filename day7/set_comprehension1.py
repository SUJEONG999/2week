a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}

print(a)
print(b)
print(a & b) # 교집합 연산자

listv = [dan * num for dan in range(1, 10) for num in range(1, 10)]  # 앞의 for 문이 밖에있는 거고, 뒤에 for 문이 안에 있는 것.. (리스트 생성)
setv =  { dan * num for dan in range(1, 10) for num in range(1, 10)}  # set로 만들어서 중복은 제외되고 생성됨.

print(listv)
print(setv)