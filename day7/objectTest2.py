l1 = [1,2,3,4,5]
l2 = l1  # 하나의 리스트를 공유하게 된다.

print(l1) #리스트 객체의 element들을 []와 함께 출력
print(l2)

print(l1[0])
print(l2[0])

print(id(l1))  # 논리적인 주소 값(참조값)
print(id(l2))  # 츨력해보니 같음(하나의 리스트를 공유해서)

l2[0] = 77  # 첫번째를 77으로 바꿈

print(l1) # 공유하고 있어서 영향 받음
print(l2)

print("*" * 30)

l3 = [1,2,3,4,5] # 리스트를 각각 만듦
l4 = [1,2,3,4,5]

print(l3)
print(l4)

print(l3[0])
print(l4[0])

print(id(l3)) # 논리적인 주소도 다름
print(id(l4))

l3[0] = 77  # l3의 첫번째원소를 77로 바꿈

print(l3)  # l3만 변경됨
print(l4)