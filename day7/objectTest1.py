a = 100
print(type(a))
print(a.bit_length())   # 100을 이진수로바꾸면 길이가 몇
print(bin(a))

b = 3.14  # 실수
print(type(b))
print(b.real)
print(b.is_integer())  # integer 아님

c = 3+4j
print(type(c))
print(c.real)
print(c.imag) # 허수부 출력

d = False
print(type(d))
print(d.bit_length())  # bool 형의 bit 길이는?
print(bin(d)) #이진수로 바꿔라

e = " "
print(type(e))  # str
print(e.isspace()) # 공백으로 되어있는가?
print(e.join("ㅋㅋㅋ"))  # blank 문자열과 ㅋㅋㅋ 같이 조인해라
# 하나씩 붙여주게 됨.(ㅋ ㅋ ㅋ)
f = []
print(type(f))
print(f.extend([1,2,3])) #또다른 리스트와 확장해라.
print(f.reverse()) # 1,2,3 을 리스트를 역순으로 바꿔라
print(f) # [3,2,1]로 나옴

print(id(a))  # 할당된 것의 논리적인 주소값
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))

