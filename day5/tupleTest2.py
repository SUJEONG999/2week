# 괄호가 없는 튜플
tuple_test = 10, 20, 30, 40  # 괄호없이 값을 여러개 줌, --> 튜플로 자동으로 패킹이 일어남.
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test:", tuple_test)
print("type(tuple_test):", type(tuple_test))   # 타입 체크했더니, 튜플로 되었음 확인
print()

# 괄호가 없는 튜플 활용
a, b, c = 10, 20, 30   # 변수를 3개를 주고 값을 여러개 줌  --> 언패킹이 일어나서 대입으로 됨.
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)
print(type(a))  # 타입 체크했더니, 숫자형으로 되었음 확인

d, e, f = "10,20,30"  # 문자열도 언패킹이 된다. a한테 10, b한테 20
print("d:", d)
print("e:", e)
print("f:", f)
