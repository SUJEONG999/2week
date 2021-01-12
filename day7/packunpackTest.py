data = [1,2,3,4]  # 리스트 생성해서 data  변수에 담음

print(data)  # 리스트 그대로 출력 []안에
print(*data)  # 아규먼트에 * 붙이면 언패킹해서 원소 값들을 하나하나 각각의 아규먼트로 전달해줌.
print(data[0], data[1], data[2], data[3])

print("*"*30)
a,b,c,d = [10,20,30,40]  # 언패킹이 일어나서 하나하나 대입된다.
print(a)
print(b)
print(c)
print(d)

print("*"*30)
x,*y,z = [10,20,30,40]   # 하나에 *붙이면 하나는 x에 주고 뒤에하나는 z 에 주고 나머지는 y에 줘,
print(x)
print(y)
print(z)

print("*"*30)
p = 100, 200, 300
print(p)   # 튜플형식
